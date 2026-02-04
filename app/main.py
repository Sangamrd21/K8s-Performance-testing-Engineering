"""
FastAPI Application with Multiple APIs for Performance Testing and Chaos Engineering
"""
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
import random
from datetime import datetime
from typing import List, Optional

app = FastAPI(
    title="Performance Testing API",
    description="APIs for learning performance testing and chaos engineering",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== Models ====================
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None

class HealthCheckResponse(BaseModel):
    status: str
    timestamp: str
    uptime_seconds: float

# ==================== In-Memory Storage ====================
items_db = {
    1: Item(id=1, name="Item 1", description="First item", price=10.0),
    2: Item(id=2, name="Item 2", description="Second item", price=20.0),
}

users_db = {
    1: User(id=1, username="john", email="john@example.com", full_name="John Doe"),
    2: User(id=2, username="jane", email="jane@example.com", full_name="Jane Doe"),
}

app_start_time = time.time()

# ==================== Health Check APIs ====================

@app.get("/health", response_model=HealthCheckResponse, tags=["Health"])
async def health_check():
    """
    Basic health check endpoint - fast response
    Good for load testing baseline
    """
    uptime = time.time() - app_start_time
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        uptime_seconds=uptime
    )

@app.get("/health/detailed", tags=["Health"])
async def detailed_health_check():
    """
    Detailed health check with system info
    Slightly heavier than basic health check
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime_seconds": time.time() - app_start_time,
        "total_items": len(items_db),
        "total_users": len(users_db),
        "api_version": "1.0.0"
    }

# ==================== Item APIs ====================

@app.get("/items", tags=["Items"])
async def list_items(skip: int = 0, limit: int = 10):
    """
    List all items with pagination
    """
    items = list(items_db.values())
    return {"items": items[skip:skip + limit], "total": len(items)}

@app.get("/items/{item_id}", tags=["Items"])
async def get_item(item_id: int):
    """
    Get a specific item by ID
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.post("/items", response_model=Item, tags=["Items"])
async def create_item(item: Item):
    """
    Create a new item
    """
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.id] = item
    return item

@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, item: Item):
    """
    Update an existing item
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

@app.delete("/items/{item_id}", tags=["Items"])
async def delete_item(item_id: int):
    """
    Delete an item
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}

# ==================== User APIs ====================

@app.get("/users", tags=["Users"])
async def list_users(skip: int = 0, limit: int = 10):
    """
    List all users with pagination
    """
    users = list(users_db.values())
    return {"users": users[skip:skip + limit], "total": len(users)}

@app.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    """
    Get a specific user by ID
    """
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users", response_model=User, tags=["Users"])
async def create_user(user: User):
    """
    Create a new user
    """
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    return user

# ==================== Performance Testing APIs ====================

@app.get("/slow-endpoint", tags=["Performance Testing"])
async def slow_endpoint(delay: int = 2):
    """
    Intentionally slow endpoint for testing performance degradation
    Use 'delay' parameter to control response time (in seconds)
    """
    if delay > 30:
        raise HTTPException(status_code=400, detail="Delay cannot exceed 30 seconds")
    time.sleep(delay)
    return {
        "message": f"Completed after {delay} seconds",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/cpu-intensive", tags=["Performance Testing"])
async def cpu_intensive(iterations: int = 1000000):
    """
    CPU-intensive operation for testing performance
    Use 'iterations' parameter to control load
    """
    if iterations > 100000000:
        raise HTTPException(status_code=400, detail="Iterations too high")
    
    result = 0
    for i in range(iterations):
        result += i ** 2
    
    return {
        "message": "CPU intensive task completed",
        "iterations": iterations,
        "result": result % 1000  # Return modulo to avoid huge numbers
    }

@app.get("/random-error", tags=["Performance Testing"])
async def random_error(failure_rate: float = 0.3):
    """
    Randomly fails based on failure_rate (0.0-1.0)
    Useful for testing error handling and recovery
    """
    if not 0 <= failure_rate <= 1:
        raise HTTPException(status_code=400, detail="Failure rate must be between 0 and 1")
    
    if random.random() < failure_rate:
        raise HTTPException(status_code=500, detail="Simulated random failure")
    
    return {"message": "Request succeeded", "failure_rate": failure_rate}

@app.get("/memory-spike", tags=["Performance Testing"])
async def memory_spike(size_mb: int = 10):
    """
    Allocates memory to simulate memory spikes
    Use 'size_mb' to control memory allocation (max 100 MB)
    """
    if size_mb > 100:
        raise HTTPException(status_code=400, detail="Size cannot exceed 100 MB")
    
    # Allocate memory
    data = "x" * (size_mb * 1024 * 1024)
    
    return {
        "message": f"Allocated {size_mb} MB",
        "data_length": len(data),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/cascade-failure", tags=["Performance Testing"])
async def cascade_failure(failure_probability: float = 0.5):
    """
    Simulates cascade failures - useful for chaos engineering
    Call this multiple times with failure_probability to simulate cascading failures
    """
    if random.random() < failure_probability:
        raise HTTPException(status_code=503, detail="Service temporarily unavailable - simulated cascade")
    
    return {"message": "Service healthy", "timestamp": datetime.now().isoformat()}

# ==================== Analytics APIs ====================

@app.get("/analytics/items-summary", tags=["Analytics"])
async def items_summary():
    """
    Get summary analytics of items
    """
    items = list(items_db.values())
    if not items:
        return {"total_items": 0, "avg_price": 0, "min_price": 0, "max_price": 0}
    
    prices = [item.price for item in items]
    return {
        "total_items": len(items),
        "avg_price": sum(prices) / len(prices),
        "min_price": min(prices),
        "max_price": max(prices),
        "total_value": sum(prices)
    }

@app.get("/analytics/users-summary", tags=["Analytics"])
async def users_summary():
    """
    Get summary analytics of users
    """
    return {
        "total_users": len(users_db),
        "user_list": list(users_db.values())
    }

# ==================== Root Endpoint ====================

@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint with API information
    """
    return {
        "message": "Welcome to Performance Testing API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
