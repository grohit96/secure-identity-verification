# app/routers/__init__.py
# Only expose health router for now
from . import health
__all__ = ["health"]
