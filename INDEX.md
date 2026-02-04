# 🎯 FastAPI Performance Testing & Chaos Engineering Lab

## 📊 Project Overview

**Status**: ✅ Complete and Ready to Use

A production-ready FastAPI application with **18 REST endpoints** designed specifically for learning:
- Performance testing & benchmarking
- Load testing & stress testing
- Chaos engineering with Litmus Chaos
- Resilience testing & failure handling

---

## 🚀 One-Minute Quick Start

```bash
# 1. Navigate to project
cd /Users/sangameshhiremath/Documents/Projects/K8s/fastapi-app

# 2. Start the application
python app/main.py

# 3. In browser, open:
# - API Docs: http://localhost:8000/docs
# - API: http://localhost:8000

# 4. In another terminal, run tests:
pytest tests/test_app.py -v
```

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| [SETUP_COMPLETE.md](SETUP_COMPLETE.md) | Complete setup summary with verification checklist |
| [README.md](README.md) | Comprehensive documentation with all features |
| [app/main.py](app/main.py) | Main application (293 lines, 18 endpoints) |
| [tests/test_app.py](tests/test_app.py) | 16 unit tests (all passing) |
| [load_test.py](load_test.py) | Locust load testing scenarios |
| [quick-start.sh](quick-start.sh) | Handy command reference |

---

## 🎯 API Endpoints Quick Reference

### Health & Monitoring
```
GET  /health              - Basic health check
GET  /health/detailed     - Detailed system status
```

### CRUD Operations
```
GET    /items             - List items
GET    /items/{id}        - Get specific item
POST   /items             - Create item
PUT    /items/{id}        - Update item
DELETE /items/{id}        - Delete item

GET    /users             - List users
GET    /users/{id}        - Get specific user
POST   /users             - Create user
```

### Performance Testing (Chaos Preparation)
```
GET  /slow-endpoint?delay=2              - Variable latency
GET  /cpu-intensive?iterations=1000000   - CPU load
GET  /random-error?failure_rate=0.3      - Error simulation
GET  /memory-spike?size_mb=10            - Memory allocation
GET  /cascade-failure?probability=0.5    - Cascade failures
```

### Analytics
```
GET  /analytics/items-summary   - Item statistics
GET  /analytics/users-summary   - User statistics
```

---

## ✨ Key Features

✅ **18 REST Endpoints** spanning CRUD, health checks, and performance testing
✅ **16 Unit Tests** - All passing, comprehensive coverage
✅ **Async/Await** - FastAPI's native async support
✅ **Data Validation** - Pydantic models
✅ **Interactive Docs** - Swagger UI at `/docs`
✅ **Docker Ready** - Production-ready container
✅ **Load Testing** - Locust integration
✅ **Health Checks** - Multiple monitoring endpoints
✅ **Error Handling** - Proper HTTP status codes
✅ **CORS Support** - Cross-origin requests enabled

---

## 📦 What's Included

```
fastapi-app/
├── app/main.py           (293 lines, well-commented)
├── tests/test_app.py     (16 unit tests)
├── load_test.py          (Locust scenarios)
├── requirements.txt      (All dependencies)
├── Dockerfile            (Production container)
├── docker-compose.yml    (Easy orchestration)
├── README.md             (Full documentation)
├── SETUP_COMPLETE.md     (Setup summary)
└── quick-start.sh        (Command reference)
```

---

## 🧪 Testing Strategies

### Unit Testing
```bash
pytest tests/test_app.py -v       # Run tests
pytest --cov=app tests/            # With coverage
```

### Load Testing
```bash
locust -f load_test.py --host=http://localhost:8000
# Open http://localhost:8089 and configure load
```

### Manual Testing
```bash
curl http://localhost:8000/health
curl http://localhost:8000/items
curl http://localhost:8000/slow-endpoint?delay=5
```

---

## 🔄 Learning Path

### Phase 1️⃣ - API Fundamentals
- ✅ Explore endpoints via `/docs`
- ✅ Understand CRUD operations
- ✅ Review test cases

### Phase 2️⃣ - Performance Testing
- 🎯 Run load tests with Locust
- 🎯 Analyze response times
- 🎯 Identify bottlenecks
- 🎯 Learn: Latency, Throughput, Error Rates

### Phase 3️⃣ - Chaos Engineering
- 🎯 Deploy to Kubernetes
- 🎯 Install Litmus Chaos
- 🎯 Run chaos experiments
- 🎯 Learn: Resilience, Recovery, Failures

---

## 🛠️ Tech Stack

| Component | Version |
|-----------|---------|
| Python | 3.12.8 |
| FastAPI | 0.104.1 |
| Uvicorn | 0.24.0 |
| Pydantic | 2.5.0 |
| pytest | 7.4.3 |
| Locust | 2.17.0 |
| Docker | Latest |

---

## 📈 Project Statistics

| Metric | Value |
|--------|-------|
| Python Files | 5 |
| Main Application Lines | 293 |
| REST Endpoints | 18 |
| Unit Tests | 16 |
| Test Pass Rate | 100% ✅ |
| Dependencies | 10 |
| Docker Compose Version | 3.8 |

---

## 🎮 Example API Calls

### Basic Health Check
```bash
curl http://localhost:8000/health
```

### List Items
```bash
curl http://localhost:8000/items
```

### Create New Item
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "name": "New Item", "price": 25.0}'
```

### Test Performance Degradation
```bash
curl http://localhost:8000/slow-endpoint?delay=5
```

### Test Error Handling
```bash
curl http://localhost:8000/random-error?failure_rate=0.7
```

### Get Analytics
```bash
curl http://localhost:8000/analytics/items-summary
```

---

## 🚢 Deployment Options

### Local Development
```bash
python app/main.py
```

### Docker
```bash
docker-compose up --build
```

### Production
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Kubernetes (Future)
Prepare for Litmus Chaos integration

---

## ✅ Verification Checklist

- [x] Virtual environment configured
- [x] Dependencies installed
- [x] 16 unit tests passing
- [x] Application runs successfully
- [x] API endpoints responding
- [x] Docker configured
- [x] Load testing setup
- [x] Documentation complete
- [x] Project ready for learning

---

## 🆘 Quick Troubleshooting

**Port 8000 already in use?**
```bash
lsof -ti:8000 | xargs kill -9
```

**Need to reinstall dependencies?**
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Docker issues?**
```bash
docker-compose down -v
docker-compose up --build
```

---

## 📞 Next Steps

1. **Start here**: Open [SETUP_COMPLETE.md](SETUP_COMPLETE.md)
2. **Explore API**: Run `python app/main.py` → Visit http://localhost:8000/docs
3. **Run tests**: Execute `pytest tests/test_app.py -v`
4. **Load test**: Use `locust -f load_test.py --host=http://localhost:8000`
5. **Go deeper**: Read [README.md](README.md) for advanced features

---

## 🎉 Ready to Start!

Your FastAPI application is completely set up and ready for:
- ✅ Learning REST API development
- ✅ Understanding performance testing
- ✅ Preparing for chaos engineering
- ✅ Building resilient systems

**Start now**: `python app/main.py` 🚀

---

*Last Updated: 2026-02-04*
*Status: Production Ready ✅*
