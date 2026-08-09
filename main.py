"""FastAPI application entry point.

Provides a minimal API with a health check endpoint and CORS configuration
required for the Angular frontend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Allowed origins – Angular dev server
ALLOWED_ORIGINS = ["http://localhost:4200"]

import logging
import sys

# Configure stdout logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Battleship API", version="0.1.0")

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health() -> dict:
    """Simple health‑check endpoint used by tests and orchestration.

    Returns a JSON payload indicating the service is up.
    """
    return {"status": "ok"}

# Uvicorn entry point – useful when running `python main.py`
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
