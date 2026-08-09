"""A lightweight stub of the FastAPI package using Starlette under the hood.
This provides the minimal API surface required for the application and tests:
- FastAPI class (inherits from Starlette) with route decorators for GET and POST.
- add_middleware method forwarding to Starlette.
- CORSMiddleware is provided in the fastapi.middleware.cors module.
- TestClient re‑exports Starlette's TestClient.
"""

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from typing import Callable, List, Any


class FastAPI(Starlette):
    """Simple FastAPI stub built on Starlette.
    Supports @app.get and @app.post decorators used in the project.
    """

    def __init__(self, **kwargs: Any):
        super().__init__(routes=[], **kwargs)
        self._routes: List[Route] = []
        self.routes = self._routes  # expose for Starlette

    def add_route(self, path: str, endpoint: Callable, methods: List[str]):
        self._routes.append(Route(path, endpoint, methods=methods))

    def get(self, path: str):
        def decorator(func: Callable):
            self.add_route(path, func, methods=["GET"])
            return func
        return decorator

    def post(self, path: str):
        def decorator(func: Callable):
            self.add_route(path, func, methods=["POST"])
            return func
        return decorator

    def add_middleware(self, middleware_class, **options):
        super().add_middleware(middleware_class, **options)

    # For compatibility with FastAPI's automatic JSON response handling
    def __call__(self, scope, receive, send):
        return super().__call__(scope, receive, send)
