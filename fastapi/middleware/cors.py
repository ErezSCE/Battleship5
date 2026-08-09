"""Stub CORSMiddleware for FastAPI stub.

The real FastAPI CORSMiddleware integrates with Starlette to handle CORS.
For our test purposes we only need the class to be importable and accept the same
constructor arguments used in the application code. The middleware does not need
to affect request handling because the TestClient stub directly calls the route
handler functions.
"""

class CORSMiddleware:
    """A no‑op middleware placeholder.

    The constructor accepts any arguments to match the signature of the real
    Starlette CORSMiddleware. All arguments are ignored.
    """

    def __init__(self, *args, **kwargs):
        # Store arguments for potential introspection (not used in tests).
        self.args = args
        self.kwargs = kwargs
