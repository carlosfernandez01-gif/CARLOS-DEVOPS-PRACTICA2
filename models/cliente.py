"""Client user model for the tienda application.

This module defines :class:`Cliente`, representing a regular customer of the
store. Clients can place orders and have a simple purchase history.
"""

from dataclasses import dataclass, field
from typing import List
from .usuario import Usuario
from .pedido import Pedido


@dataclass
class Cliente(Usuario):
    """A client user who can place orders in the tienda."""

    historial_pedidos: List[Pedido] = field(default_factory=list)

    def agregar_pedido(self, pedido: Pedido) -> None:
        """Add a new order to the client's purchase history."""
        self.historial_pedidos.append(pedido)

    def es_administrador(self) -> bool:
        return False