"""Model package for the tienda application.

This package exposes the core domain objects used by the tienda application,
including products, users and orders. Each module defines a small class
hierarchy appropriate for its concept. All classes implement simple,
well‑documented APIs so that other parts of the application, such as the
service layer, can use them without knowing their internal details.

The intention of this package is educational: it demonstrates basic
object‑oriented design in Python for a small retail domain. You could
extend or modify these classes to suit more complex requirements.
"""

from .producto import Producto
from .producto_electronico import ProductoElectronico
from .producto_ropa import ProductoRopa
from .usuario import Usuario
from .cliente import Cliente
from .administrador import Administrador
from .pedido import Pedido

__all__ = [
    "Producto",
    "ProductoElectronico",
    "ProductoRopa",
    "Usuario",
    "Cliente",
    "Administrador",
    "Pedido",
]