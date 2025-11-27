from dataclasses import dataclass
from .producto import Producto


@dataclass(frozen=True)
class ProductoRopa(Producto):
    talla: str
    color: str

    def __str__(self) -> str:
        return (
            f"{self.nombre} (ID {self.id}) - {self.precio:.2f} € "
            f"- Talla {self.talla} Color {self.color}"
        )
