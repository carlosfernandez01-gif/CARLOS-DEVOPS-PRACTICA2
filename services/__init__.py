"""Service layer for the tienda application.

This package provides high‑level services that operate on the domain models.
In a larger application this layer would contain business logic and
coordinate between models, repositories and external systems. Here it
contains just a simple service for managing products.
"""

from .tienda_service import TiendaService  # noqa: F401

__all__ = ["TiendaService"]