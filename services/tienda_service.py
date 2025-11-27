"""Servicio principal de la tienda.

Se encarga de gestionar el catálogo de productos y la creación de pedidos.
"""

from typing import Dict, List

from models.producto import Producto
from models.producto_electronico import ProductoElectronico
from models.producto_ropa import ProductoRopa
from models.pedido import Pedido


class TiendaService:
    """Servicio que gestiona productos y pedidos en memoria."""

    def __init__(self) -> None:
        # Diccionario id -> producto
        self._productos: Dict[int, Producto] = {}

    # ---------- Productos ----------

    @staticmethod
    def productos_demo() -> List[Producto]:
        """Devuelve una lista de productos de ejemplo."""
        return [
            ProductoElectronico(nombre="ExampleTech Smartphone", precio=399.0, meses_garantia=24),
            ProductoElectronico(nombre="ExampleTech Portátil", precio=899.0, meses_garantia=24),
            ProductoRopa(nombre="Camiseta", precio=19.99, talla="M", color="Azul"),
            ProductoRopa(nombre="Pantalón", precio=39.99, talla="L", color="Negro"),
        ]

    def agregar_producto(self, producto: Producto) -> None:
        """Añade un producto al catálogo."""
        self._productos[producto.id] = producto

    def listar_productos(self) -> List[str]:
        """Devuelve una lista de descripciones de los productos."""
        return [str(p) for p in self._productos.values()]

    # ---------- Pedidos ----------

    def crear_pedido(self, ids_productos: List[int]) -> Pedido:
        """Crea un pedido a partir de una lista de IDs de productos."""
        productos_seleccionados: List[Producto] = []
        for pid in ids_productos:
            producto = self._productos.get(pid)
            if producto is None:
                raise ValueError(f"No existe producto con id {pid}")
            productos_seleccionados.append(producto)

        pedido = Pedido(productos=productos_seleccionados)
        return pedido
