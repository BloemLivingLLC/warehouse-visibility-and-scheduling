import os
import time
import httpx


class InforClient:
    def __init__(self):
        # API settings will come from environment variables
        self.base_url = os.getenv("INFOR_BASE_URL")
        self.token_url = os.getenv("INFOR_TOKEN_URL")
        self.client_id = os.getenv("INFOR_CLIENT_ID")
        self.client_secret = os.getenv("INFOR_CLIENT_SECRET")
        self.username = os.getenv("INFOR_USERNAME")

        self.access_token = None
        self.token_expires_at = 0

    def get_headers(self):
        # Headers we'll use when making WMS API requests
        if not self.access_token:
            raise ValueError("No access token available")

        return {
            "Authorization": f"Bearer {self.access_token}",
            "Username": self.username,
            "Accept": "application/json"
        }

    def authenticate(self):
        # Check if the required settings are available
        if not all([
            self.token_url,
            self.client_id,
            self.client_secret
        ]):
            raise ValueError("Missing Infor API credentials")

        # Request an access token
        response = httpx.post(
            self.token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            },
            timeout=30
        )

        response.raise_for_status()

        
        # Save the token and its expiration time
        token_data = response.json()
        self.access_token = token_data["access_token"]

        # Refresh the token 60 seconds before it expires
        expires_in = int(token_data["expires_in"])
        self.token_expires_at = time.monotonic() + max(0, expires_in - 60)

        return self.access_token

    def get(self, endpoint):
        # Make sure we have an access token
        if not self.access_token or time.monotonic() >= self.token_expires_at:
            self.authenticate()

        # Check that the API URL and username are available
        if not self.base_url or not self.username:
            raise ValueError("Missing Infor API settings")

        # Send the request to Infor WMS
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        response = httpx.get(
            url,
            headers=self.get_headers(),
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, data=None):
        # Get a token if we don't have one
        if not self.access_token or time.monotonic() >= self.token_expires_at:
            self.authenticate()

        if not self.base_url or not self.username:
            raise ValueError("Missing Infor API settings")

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

        request_options = {
            "headers": self.get_headers(),
            "timeout": 120
        }

        if data is not None:
            request_options["json"] = data

        response = httpx.post(url, **request_options)

        response.raise_for_status()

        return response.json()
