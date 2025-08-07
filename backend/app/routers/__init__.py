# app/routers/__init__.py
# Only expose health router for now
from . import health, users
__all__ = ["health", "users"]
