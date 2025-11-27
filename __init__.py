"""Top‑level package for the tienda application.

This file marks the ``tienda_app`` directory as a package and exports the
service layer and models for convenience. It also defines a module level
``__all__`` variable to control what is imported when doing ``from
tienda_app import *``.
"""

from . import models
from .services import TiendaService  # noqa: F401

__all__ = ["models", "TiendaService"]