from dataclasses import dataclass, field
from typing import ClassVar
import itertools


@dataclass(frozen=True)
class Producto:
    """Clase base para todos los productos de la tienda.

    Genera un identificador único automáticamente para cada instancia.
    """

    # Contador interno de IDs (compartido por todas las instancias)
    _id_counter: ClassVar[itertools.count] = itertools.count(1)

    # Atributos que se pasan al crear el producto
    nombre: str
    precio: float

    # El ID se rellena automáticamente en __post_init__
    id: int = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "id", next(self._id_counter))

    def __str__(self) -> str:
        return f"{self.nombre} (ID {self.id}) - {self.precio:.2f} €"
