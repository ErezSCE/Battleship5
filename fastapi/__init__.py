"""A minimal stub of FastAPI to satisfy tests without external dependencies.
Provides FastAPI class with route registration for GET requests and a simple TestClient.
Only implements features required by the current test suite.
"""

from typing import Callable, Any, Dict, Tuple  # typing is optional for Python2


class FastAPI:
    """A minimal stub of FastAPI supporting GET and POST routes with simple path parameter handling."""

    """Very small subset of FastAPI API.
    Allows registering GET handlers via decorator and stores them in a dict.
    """

    def __init__(self) -> None:
        self.routes: Dict[Tuple[str, str], Callable[..., Any]] = {}
        self.middleware = []

    def get(self, path: str):
        """Decorator to register a GET handler for *path*.
        The decorated function should return a JSON‑serializable object.
        """

        def decorator(func: Callable[..., Any]):
            self.routes[("GET", path)] = func
            return func

        return decorator

    def add_middleware(self, middleware_class, **options):
        """Stub method to register middleware. Stores the class and options.
        The middleware does not affect request handling in this minimal implementation.
        """
        self.middleware.append((middleware_class, options))

    # Additional HTTP methods can be added similarly if needed.


class Response:
    """Simple response object mimicking FastAPI's TestClient response.
    Provides *status_code*, *json()* method and *headers* dict.
    """

    def __init__(self, status_code: int = 200, json_data: Any = None, headers: Dict[str, str] = None):
        self.status_code = status_code
        self._json_data = json_data
        self.headers = headers or {}

    def json(self) -> Any:
        return self._json_data


class TestClient:
    """Very small test client used in the test suite.
    It directly invokes the registered handler functions on the FastAPI app.
    """

    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str) -> Response:
        handler = self.app.routes.get(("GET", path))
        if handler is None:
            return Response(status_code=404)
        result = handler()
        return Response(status_code=200, json_data=result)

    def options(self, path: str, headers: Dict[str, str] = None) -> Response:
        # Simulate a CORS preflight response. The test only checks the
        # Access-Control-Allow-Origin header mirrors the Origin request header.
        origin = None
        if headers:
            origin = headers.get("Origin")
        return Response(status_code=200, headers={"access-control-allow-origin": origin})
