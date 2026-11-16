import httpx
from fastapi import FastAPI, HTTPException
from infor_client import InforClient

app = FastAPI(
    title="Bloem Warehouse Visibility API",
    description="Backend API for the Bloem warehouse visibility and scheduling project",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Bloem Warehouse Visibility API"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "Backend is running"
    }


# Convert Infor shipment data into the format our frontend uses
def format_shipment(s):
    # Handle field names from both list and detail responses
    customer = s.get("c_company") or s.get("ccompany") or ""
    city = s.get("c_city") or s.get("ccity") or ""
    state = s.get("c_state") or s.get("cstate") or ""

    destination = ", ".join(
        part for part in [city, state] if part
    )

    return {
        "orderkey": s.get("orderkey"),
        "order_number": s.get("externorderkey") or s.get("orderkey") or "",
        "status": s.get("status") or "",
        "carrier": s.get("carriername") or "",
        "ship_date": s.get("actualshipdate") or None,
        "load_id": s.get("loadid") or "",
        "customer": customer,
        "warehouse": s.get("whseid") or "",
        "destination": destination,
        "weight_lbs": None,
        "pallet_count": s.get("totalpalletestimate")
    }


# Get shipments from Infor WMS
@app.get("/api/shipments")
def get_shipments():
    try:
        client = InforClient()

        records = client.post(
            "bodlist/showshipmentorderlist?recordcount=5"
        )

        shipments = []

        for record in records:
            shipment = format_shipment(record)
            orderkey = record.get("orderkey")

            # Get additional details for this shipment
            if orderkey:
                try:
                    detail = client.get(f"shipments/{orderkey}")

                    if isinstance(detail, list):
                        detail = detail[0] if detail else {}

                    if isinstance(detail, dict):
                        shipment["ship_date"] = (
                            detail.get("actualshipdate") or None
                        )

                        shipment["pallet_count"] = (
                            detail.get("totalpalletestimate")
                        )

                        # Keep weight empty until its unit is confirmed
                        shipment["weight_lbs"] = None

                except httpx.HTTPError:
                    # Keep the basic shipment if details fail
                    pass

            shipments.append(shipment)

        return shipments

    except (httpx.HTTPError, ValueError, KeyError):
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve shipments from Infor WMS"
        )


# Get one shipment by orderkey
@app.get("/api/shipments/{orderkey}")
def get_shipment(orderkey: str):
    try:
        client = InforClient()

        shipment = client.get(f"shipments/{orderkey}")

        if isinstance(shipment, list):
            if not shipment:
                raise HTTPException(
                    status_code=404,
                    detail="Shipment not found"
                )
            shipment = shipment[0]

        return format_shipment(shipment)

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Shipment not found"
            )

        raise HTTPException(
            status_code=502,
            detail="Infor WMS request failed"
        )

    except (httpx.HTTPError, ValueError, KeyError):
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve shipment from Infor WMS"
        )
