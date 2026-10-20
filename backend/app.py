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
        "load_id": "LOAD-101",
        "customer": "Walmart",
        "warehouse": "WM01",
        "destination": "Bentonville, AR",
        "weight_lbs": 18500,
        "pallet_count": 22
    },
    {
        "orderkey": 1002,
        "order_number": "ORD-1002",
        "status": "Shipped",
        "carrier": "Carrier B",
        "ship_date": "2026-10-18",
        "load_id": "LOAD-102",
        "customer": "Menards",
        "warehouse": "WM02",
        "destination": "Grand Rapids, MI",
        "weight_lbs": 20000,
        "pallet_count": 30
    },
    {
        "orderkey": 1003,
        "order_number": "ORD-1003",
        "status": "Scheduled",
        "carrier": "Carrier C",
        "ship_date": "2026-10-22",
        "load_id": "LOAD-103",
        "customer": "Lowe's",
        "warehouse": "WM03",
        "destination": "Lansing, MI",
        "weight_lbs": 15500,
        "pallet_count": 18
    },
    {
        "orderkey": 1004,
        "order_number": "ORD-1004",
        "status": "Pending",
        "carrier": "Carrier A",
        "ship_date": "2026-10-24",
        "load_id": "LOAD-104",
        "customer": "Home Depot",
        "warehouse": "WM01",
        "destination": "Atlanta, GA",
        "weight_lbs": 22000,
        "pallet_count": 26
    },
    {
        "orderkey": 1005,
        "order_number": "ORD-1005",
        "status": "Scheduled",
        "carrier": "Carrier B",
        "ship_date": "2026-10-21",
        "load_id": "LOAD-105",
        "customer": "Walmart",
        "warehouse": "WM02",
        "destination": "Bentonville, AR",
        "weight_lbs": 19800,
        "pallet_count": 24
    },
    {
        "orderkey": 1006,
        "order_number": "ORD-1006",
        "status": "Shipped",
        "carrier": "Carrier C",
        "ship_date": "2026-10-16",
        "load_id": "LOAD-106",
        "customer": "ACE Hardware",
        "warehouse": "WM03",
        "destination": "Oak Brook, IL",
        "weight_lbs": 9600,
        "pallet_count": 12
    },
    {
        "orderkey": 1007,
        "order_number": "ORD-1007",
        "status": "Scheduled",
        "carrier": "Carrier A",
        "ship_date": "2026-10-23",
        "load_id": "LOAD-107",
        "customer": "Lowe's",
        "warehouse": "WM01",
        "destination": "Mooresville, NC",
        "weight_lbs": 17200,
        "pallet_count": 20
    },
    {
        "orderkey": 1008,
        "order_number": "ORD-1008",
        "status": "Pending",
        "carrier": "Carrier B",
        "ship_date": "2026-10-28",
        "load_id": "LOAD-108",
        "customer": "Menards",
        "warehouse": "WM02",
        "destination": "Eau Claire, WI",
        "weight_lbs": 21400,
        "pallet_count": 28
    },
    {
        "orderkey": 1009,
        "order_number": "ORD-1009",
        "status": "Shipped",
        "carrier": "Carrier C",
        "ship_date": "2026-10-17",
        "load_id": "LOAD-109",
        "customer": "Home Depot",
        "warehouse": "WM03",
        "destination": "Detroit, MI",
        "weight_lbs": 14300,
        "pallet_count": 16
    },
    {
        "orderkey": 1010,
        "order_number": "ORD-1010",
        "status": "Scheduled",
        "carrier": "Carrier A",
        "ship_date": "2026-10-25",
        "load_id": "LOAD-110",
        "customer": "Walmart",
        "warehouse": "WM01",
        "destination": "Grand Rapids, MI",
        "weight_lbs": 23000,
        "pallet_count": 30
    },
    {
        "orderkey": 1011,
        "order_number": "ORD-1011",
        "status": "Pending",
        "carrier": "Carrier B",
        "ship_date": "2026-10-30",
        "load_id": "LOAD-111",
        "customer": "ACE Hardware",
        "warehouse": "WM02",
        "destination": "Lansing, MI",
        "weight_lbs": 8800,
        "pallet_count": 10
    },
    {
        "orderkey": 1012,
        "order_number": "ORD-1012",
        "status": "Shipped",
        "carrier": "Carrier C",
        "ship_date": "2026-10-19",
        "load_id": "LOAD-112",
        "customer": "Lowe's",
        "warehouse": "WM03",
        "destination": "Columbus, OH",
        "weight_lbs": 16700,
        "pallet_count": 19
    },
    {
        "orderkey": 1013,
        "order_number": "ORD-1013",
        "status": "Scheduled",
        "carrier": "Carrier A",
        "ship_date": "2026-10-27",
        "load_id": "LOAD-113",
        "customer": "Home Depot",
        "warehouse": "WM01",
        "destination": "Indianapolis, IN",
        "weight_lbs": 20500,
        "pallet_count": 25
    },
    {
        "orderkey": 1014,
        "order_number": "ORD-1014",
        "status": "Scheduled",
        "carrier": "Carrier B",
        "ship_date": "2026-10-29",
        "load_id": "LOAD-114",
        "customer": "Menards",
        "warehouse": "WM02",
        "destination": "Fort Wayne, IN",
        "weight_lbs": 18900,
        "pallet_count": 23
    },
    {
        "orderkey": 1015,
        "order_number": "ORD-1015",
        "status": "Pending",
        "carrier": "Carrier C",
        "ship_date": "2026-11-02",
        "load_id": "LOAD-115",
        "customer": "Walmart",
        "warehouse": "WM03",
        "destination": "Chicago, IL",
        "weight_lbs": 24000,
        "pallet_count": 32
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
