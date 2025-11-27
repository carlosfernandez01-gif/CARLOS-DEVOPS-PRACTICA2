from services import TiendaService


def main() -> None:
    """Punto de entrada de la aplicación de tienda.

    Carga unos productos de ejemplo, los muestra por pantalla y pide al usuario
    que introduzca los IDs de los productos que quiere comprar.
    """
    service = TiendaService()

    # Cargamos productos de ejemplo en el catálogo
    for producto in TiendaService.productos_demo():
        service.agregar_producto(producto)

    print("Bienvenido a la Tienda!")
    print("Productos disponibles:")
    for descripcion in service.listar_productos():
        print("  -", descripcion)

    entrada = input(
        "\nIntroduzca los IDs de los productos que desea comprar, separados por coma: "
    )

    try:
        ids = [int(x.strip()) for x in entrada.split(",") if x.strip()]
    except ValueError:
        print("Entrada no válida. Introduzca solo números separados por coma.")
        return

    pedido = service.crear_pedido(ids)
    print("\nSu pedido:")
    print(pedido)


if __name__ == "__main__":
    main()
