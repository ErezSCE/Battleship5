import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    """Ensure the health check endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_cors_headers():
    """Check that CORS headers are present for allowed origin."""
    origin = "http://localhost:4200"
    response = client.options(
        "/health",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "GET",
        },
    )
    # FastAPI returns 200 for preflight with proper CORS config
    assert response.status_code == 200
    # The Access-Control-Allow-Origin header should echo the allowed origin
    assert response.headers.get("access-control-allow-origin") == origin
