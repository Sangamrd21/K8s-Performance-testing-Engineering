#!/bin/bash

# FastAPI Application Quick Start Guide
# This script provides helpful commands for common tasks

echo "=== FastAPI Performance Testing Application ==="
echo ""

# Check if Python environment is set up
if [ ! -d "venv" ]; then
    echo "Setting up Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

source venv/bin/activate

echo ""
echo "Quick Commands:"
echo "==============="
echo ""
echo "1. Start the application:"
echo "   python app/main.py"
echo "   OR"
echo "   uvicorn app.main:app --reload"
echo ""
echo "2. Run unit tests:"
echo "   pytest tests/test_app.py -v"
echo ""
echo "3. Run all tests with coverage:"
echo "   pytest --cov=app tests/"
echo ""
echo "4. Start load testing (requires app running in another terminal):"
echo "   locust -f load_test.py --host=http://localhost:8000"
echo ""
echo "5. Build Docker image:"
echo "   docker build -t fastapi-app:latest ."
echo ""
echo "6. Run with Docker Compose:"
echo "   docker-compose up --build"
echo ""
echo "7. Test API endpoints:"
echo "   curl http://localhost:8000/health"
echo "   curl http://localhost:8000/items"
echo "   curl http://localhost:8000/docs  (Swagger UI)"
echo ""
echo "8. Create a new item:"
echo "   curl -X POST http://localhost:8000/items \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"id\":3,\"name\":\"New Item\",\"price\":25.0}'"
echo ""
echo "9. Test slow endpoint (for performance testing):"
echo "   curl http://localhost:8000/slow-endpoint?delay=3"
echo ""
echo "10. Test random errors:"
echo "    curl http://localhost:8000/random-error?failure_rate=0.5"
echo ""
echo "Available at:"
echo "============="
echo "API Docs:  http://localhost:8000/docs"
echo "ReDoc:     http://localhost:8000/redoc"
echo "Health:    http://localhost:8000/health"
echo ""
echo "For more information, see README.md"
