"""Main application entry point for the Battleship API.

Provides a minimal FastAPI app with a health check endpoint.
The stub FastAPI implementation in this repository supplies only the
features required for the test suite.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health() -> dict:
    """Health check endpoint returning a simple status payload."""
    return {"status": "ok"}
