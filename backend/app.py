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
    return {
        "orderkey": s.get("orderkey"),
        "order_number": s.get("externalorderkey") or s.get("orderkey") or "",
        "status": s.get("status") or "",
        "carrier": s.get("carriername") or "",
        "ship_date": None,
        "load_id": s.get("loadid") or "",
        "customer": "",
        "warehouse": "",
        "destination": "",
        "weight_lbs": None,
        "pallet_count": None
    }


# Get shipments from Infor WMS
@app.get("/api/shipments")
def get_shipments():
    try:
        client = InforClient()

        records = client.post(
            "bodlist/showshipmentorderlist?recordcount=5"
        )

        return [format_shipment(s) for s in records]

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
