# FastAPI Performance Testing Application - Setup Guide

## Project Overview
FastAPI application with multiple APIs for learning performance testing and chaos engineering with Litmus Chaos.

## Setup Checklist

- [x] Project Structure Created
  - FastAPI main application with 15+ endpoints
  - Unit tests with pytest
  - Load testing script with Locust
  - Docker and Docker Compose configuration
  - Complete README documentation

- [x] Dependencies Configured
  - FastAPI and Uvicorn for API framework
  - Pydantic for data validation
  - Pytest for testing
  - Locust for load testing
  - All specified in requirements.txt

- [x] API Endpoints Implemented
  - Health checks (basic and detailed)
  - CRUD operations for items and users
  - Performance testing endpoints (slow, CPU-intensive, errors, memory)
  - Analytics endpoints
  - Chaos engineering simulation endpoints

- [x] Testing Infrastructure
  - Unit tests covering all endpoints
  - Load testing script with realistic user patterns
  - pytest configuration for local testing

- [x] Containerization
  - Dockerfile with health checks
  - Docker Compose for easy local development
  - .dockerignore for optimized builds

## Next Steps

### For Local Development:
1. Create and activate virtual environment: `python3 -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run application: `uvicorn app.main:app --reload`
4. Access at `http://localhost:8000` and docs at `http://localhost:8000/docs`

### For Docker Development:
1. Build and run: `docker-compose up --build`
2. Application runs at `http://localhost:8000`

### For Testing:
1. Unit tests: `pytest` or `pytest -v`
2. Load testing: `locust -f load_test.py --host=http://localhost:8000`

### For Chaos Engineering (Future):
1. Deploy to Kubernetes
2. Install Litmus Chaos
3. Run chaos experiments on the performance testing endpoints

## Project Features

- 15+ REST API endpoints covering CRUD operations
- Built-in performance testing endpoints for chaos engineering
- Full test coverage with pytest
- Production-ready Docker setup
- Load testing capabilities with Locust
- Interactive Swagger UI and ReDoc documentation
- In-memory data storage for simplicity
- CORS middleware for cross-origin requests

## Key Files

- `app/main.py` - Main FastAPI application (300+ lines, well-commented)
- `tests/test_app.py` - Comprehensive unit tests
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration with health checks
- `docker-compose.yml` - Docker Compose for local development
- `load_test.py` - Locust load testing scenarios
- `README.md` - Detailed documentation

## Architecture Notes

- In-memory storage (can be replaced with databases)
- Async-ready with FastAPI
- Modular endpoint design
- Built-in error handling and validation
- Performance testing endpoints with configurable parameters
