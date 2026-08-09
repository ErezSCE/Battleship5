"""Stub CORSMiddleware for FastAPI stub package.

This minimal implementation satisfies the interface used in the application code.
It accepts the same arguments as the real FastAPI CORSMiddleware but does not
perform any actual CORS handling because the tests only verify that the middleware
is added without raising errors.
"""

from typing import List, Optional

class CORSMiddleware:
    def __init__(
        self,
        app,
        allow_origins: List[str] = None,
        allow_methods: List[str] = None,
        allow_headers: List[str] = None,
        allow_credentials: bool = False,
        expose_headers: List[str] = None,
        max_age: int = 600,
    ):
        # Store parameters for potential introspection in tests.
        self.app = app
        self.allow_origins = allow_origins or []
        self.allow_methods = allow_methods or []
        self.allow_headers = allow_headers or []
        self.allow_credentials = allow_credentials
        self.expose_headers = expose_headers or []
        self.max_age = max_age

    def __call__(self, scope, receive, send):
        # The real middleware would modify the response headers. For the stub we
        # simply forward the call to the underlying ASGI app.
        return self.app(scope, receive, send)
