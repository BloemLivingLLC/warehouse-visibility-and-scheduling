from fastapi import FastAPI

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
