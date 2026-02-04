"""
Locust load testing script for FastAPI application
Run with: locust -f load_test.py --host=http://localhost:8000
"""
from locust import HttpUser, task, between
import random

class APIUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between requests
    
    @task(10)
    def health_check(self):
        """Health check endpoint - most frequent"""
        self.client.get("/health")
    
    @task(8)
    def list_items(self):
        """List items endpoint"""
        self.client.get("/items")
    
    @task(8)
    def list_users(self):
        """List users endpoint"""
        self.client.get("/users")
    
    @task(5)
    def get_item(self):
        """Get specific item"""
        item_id = random.randint(1, 2)
        self.client.get(f"/items/{item_id}")
    
    @task(5)
    def get_user(self):
        """Get specific user"""
        user_id = random.randint(1, 2)
        self.client.get(f"/users/{user_id}")
    
    @task(3)
    def slow_endpoint(self):
        """Test slow endpoint"""
        self.client.get("/slow-endpoint?delay=1")
    
    @task(2)
    def random_error(self):
        """Test random error endpoint"""
        self.client.get("/random-error?failure_rate=0.2")
    
    @task(1)
    def cpu_intensive(self):
        """Test CPU intensive endpoint"""
        self.client.get("/cpu-intensive?iterations=100000")
    
    @task(2)
    def analytics(self):
        """Get analytics"""
        choice = random.choice([
            "/analytics/items-summary",
            "/analytics/users-summary"
        ])
        self.client.get(choice)
