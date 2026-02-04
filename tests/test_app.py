"""
Unit tests for FastAPI Application
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ==================== Health Check Tests ====================

def test_health_check():
    """Test basic health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["uptime_seconds"] >= 0

def test_detailed_health_check():
    """Test detailed health check endpoint"""
    response = client.get("/health/detailed")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "total_items" in data
    assert "total_users" in data

# ==================== Item Tests ====================

def test_list_items():
    """Test listing items"""
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data

def test_get_item():
    """Test getting a specific item"""
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data

def test_get_nonexistent_item():
    """Test getting non-existent item"""
    response = client.get("/items/9999")
    assert response.status_code == 404

def test_create_item():
    """Test creating a new item"""
    new_item = {
        "id": 999,
        "name": "Test Item",
        "description": "Test Description",
        "price": 99.99
    }
    response = client.post("/items", json=new_item)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"

def test_delete_item():
    """Test deleting an item"""
    # First create an item
    new_item = {
        "id": 998,
        "name": "To Delete",
        "price": 10.0
    }
    client.post("/items", json=new_item)
    
    # Then delete it
    response = client.delete("/items/998")
    assert response.status_code == 200
    
    # Verify it's deleted
    response = client.get("/items/998")
    assert response.status_code == 404

# ==================== User Tests ====================

def test_list_users():
    """Test listing users"""
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert "total" in data

def test_get_user():
    """Test getting a specific user"""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data

def test_create_user():
    """Test creating a new user"""
    new_user = {
        "id": 999,
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    response = client.post("/users", json=new_user)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"

# ==================== Performance Testing Endpoints ====================

def test_random_error_endpoint():
    """Test random error endpoint"""
    response = client.get("/random-error?failure_rate=0")
    assert response.status_code == 200

def test_memory_spike_endpoint():
    """Test memory spike endpoint"""
    response = client.get("/memory-spike?size_mb=5")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_cpu_intensive_endpoint():
    """Test CPU intensive endpoint"""
    response = client.get("/cpu-intensive?iterations=100000")
    assert response.status_code == 200
    data = response.json()
    assert "result" in data

# ==================== Analytics Tests ====================

def test_items_summary():
    """Test items summary endpoint"""
    response = client.get("/analytics/items-summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_items" in data
    assert "avg_price" in data

def test_users_summary():
    """Test users summary endpoint"""
    response = client.get("/analytics/users-summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_users" in data

# ==================== Root Endpoint Test ====================

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
