from dataclasses import dataclass, field
from typing import List
from .producto import Producto


@dataclass(frozen=True)
class Pedido:
    productos: List[Producto] = field(default_factory=list)

    def total(self) -> float:
        """Calcula el total del pedido."""
        return sum(p.precio for p in self.productos)

    def __str__(self) -> str:
        """Devuelve un resumen del pedido."""
        lineas = [str(p) for p in self.productos]  # ← usamos __str__(), no descripcion()
        texto_productos = "\n".join(lineas)
        return f"{texto_productos}\nTotal: {self.total():.2f} €"
