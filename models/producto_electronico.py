from dataclasses import dataclass
from .producto import Producto


@dataclass(frozen=True)
class ProductoElectronico(Producto):
    meses_garantia: int

    def __str__(self) -> str:
        return (
            f"{self.nombre} (ID {self.id}) - {self.precio:.2f} € "
            f"- Garantía {self.meses_garantia} meses"
        )

