"""Base user model for the tienda application.

The :class:`Usuario` class represents a generic user of the tienda system. It
contains basic identifying information such as a unique identifier and
username. Subclasses differentiate between clients and administrators.
"""

from dataclasses import dataclass


@dataclass
class Usuario:
    """A generic user with an identifier and username."""

    id: int
    nombre: str

    def es_administrador(self) -> bool:
        """Return ``True`` if this user is an administrator.

        Subclasses should override this method to indicate their type.
        """
        return False