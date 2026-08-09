import logging
import sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Configure stdout logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health", response_class=JSONResponse)
def health_check() -> dict:
    """Simple health‑check endpoint.

    Returns:
        A JSON object with a ``status`` key set to ``"ok"``.
    """
    logger.info("Health check requested")
    return {"status": "ok"}
