"""Administrator user model for the tienda application.

Administrators have additional privileges, such as managing products or
orders. In this simplified model, the class simply overrides a method to
indicate that it is an administrator.
"""

from dataclasses import dataclass
from .usuario import Usuario


@dataclass
class Administrador(Usuario):
    """A user with administrative privileges."""

    def es_administrador(self) -> bool:
        return True