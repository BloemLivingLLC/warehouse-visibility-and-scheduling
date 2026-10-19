import time
import httpx
from unittest.mock import patch
from infor_client import InforClient


def mock_request(request):
    # Return fake shipment data
    return httpx.Response(
        200,
        json={"shipments": [{"orderkey": 1001, "status": "Scheduled"}]},
        request=httpx.Request("GET", "https://example.com")
    )


client = InforClient()

# Temporary test settings
client.base_url = "https://example.com"
client.username = "test_user"
client.access_token = "fake_token"
client.token_expires_at = time.monotonic() + 3600

# Intercept requests so nothing is sent to Infor
with patch("infor_client.httpx.get", return_value=mock_request(None)) as mock_get:
    result = client.get("shipments/1001")
    assert result["shipments"][0]["orderkey"] == 1001
    assert mock_get.call_args.kwargs["headers"]["Authorization"] == "Bearer fake_token"
    print("GET request test passed")

with patch("infor_client.httpx.post", return_value=mock_request(None)) as mock_post:
    result = client.post("bodlist/showshipmentorderlist", {})
    assert result["shipments"][0]["orderkey"] == 1001
    assert mock_post.call_args.kwargs["json"] == {}
    print("POST request test passed")

# Test an expired token
client.access_token = "expired_token"
client.token_expires_at = 0

with patch.object(client, "authenticate", return_value="new_token") as mock_auth:
    with patch("infor_client.httpx.get", return_value=mock_request(None)):
        client.get("shipments/1001")
        mock_auth.assert_called_once()
        print("Token expiration test passed")

# Test POST request without a JSON body
client.access_token = "fake_token"
client.token_expires_at = time.monotonic() + 3600

with patch("infor_client.httpx.post", return_value=mock_request(None)) as mock_post:
    client.post("inventorybalance/showinventorybalancelist")

    assert "json" not in mock_post.call_args.kwargs
    print("POST without body test passed")
