from fastapi import FastAPI, HTTPException

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


# Mock shipment data for testing
shipments = [
    {
        "orderkey": 1001,
        "order_number": "ORD-1001",
        "status": "Scheduled",
        "carrier": "Carrier A",
        "ship_date": "2026-10-20",
        "load_id": "LOAD-101"
    },
    {
        "orderkey": 1002,
        "order_number": "ORD-1002",
        "status": "Shipped",
        "carrier": "Carrier B",
        "ship_date": "2026-10-18",
        "load_id": "LOAD-102"
    },
    {
        "orderkey": 1003,
        "order_number": "ORD-1003",
        "status": "Scheduled",
        "carrier": "Carrier C",
        "ship_date": "2026-10-22",
        "load_id": "LOAD-103"
    }
]


# Get all shipments
@app.get("/api/shipments")
def get_shipments():
    return shipments


# Get one shipment by orderkey
@app.get("/api/shipments/{orderkey}")
def get_shipment(orderkey: int):
    for shipment in shipments:
        if shipment["orderkey"] == orderkey:
            return shipment

    raise HTTPException(status_code=404, detail="Shipment not found")
