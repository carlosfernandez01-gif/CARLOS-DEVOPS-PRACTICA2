# Tienda Online – Práctica de DevOps

Este proyecto implementa una tienda online sencilla en Python como parte de
una práctica de la asignatura de Arquitectura del Software. Contiene un
conjunto de clases que representan productos (electrónicos y ropa), usuarios
(clientes y administradores) y pedidos. Además se proporciona un servicio
(`TiendaService`) para administrar el catálogo y crear pedidos, así como un
programa principal (`main.py`) que permite al usuario seleccionar productos
por consola y calcula el total de la compra.

## Estructura del código

```
tienda_app/
    models/
        __init__.py      # Exporta las clases de dominio
        producto.py      # Clase base Producto
        producto_electronico.py
        producto_ropa.py
        usuario.py
        cliente.py
        administrador.py
        pedido.py        # Representa un pedido con productos
    services/
        __init__.py
        tienda_service.py
    main.py              # Punto de entrada de la aplicación
    Dockerfile           # Contiene la definición de la imagen Docker
    requirements.txt     # Lista de dependencias (vacía en este ejemplo)
    .dockerignore        # Archivos a excluir del contexto de build
```

## Uso sin Docker

Se recomienda utilizar un entorno virtual para instalar dependencias, aunque
este proyecto no tiene dependencias externas. Para ejecutar la aplicación
utilice la opción de módulos de Python. Desde el directorio que contiene
la carpeta ``tienda_app`` ejecute:

```bash
python -m tienda_app.main
```

El programa mostrará los productos disponibles y solicitará los IDs de los
productos que desea comprar. A continuación imprimirá un resumen del
pedido con el total.

## Uso con Docker

Para contenerizar la aplicación se proporciona un `Dockerfile` basado en
`python:3.12-slim`. Este fichero copia el código, instala las
dependencias declaradas en `requirements.txt` y define el comando de
ejecución del servicio.

### Construcción de la imagen

Ejecute el siguiente comando desde la raíz del proyecto para construir
la imagen:

```bash
docker build -t tienda-online:1.0 .
```

### Ejecución de la imagen

Para ejecutar el contenedor y probar la aplicación:

```bash
docker run --rm -it tienda-online:1.0
```

La opción `-it` permite introducir por teclado los IDs de los productos.

### Variables de entorno

Esta aplicación no necesita variables de entorno especiales. En entornos
reales se podrían añadir variables para configurar, por ejemplo, un
servidor de base de datos o claves de API.

## Desarrollo y contribución

Este repositorio es una práctica educativa. Si desea ampliarlo o
adaptarlo a sus necesidades, puede hacerlo libremente. Algunas ideas para
seguir desarrollando son:

* Persistir datos en una base de datos real.
* Añadir autenticación de usuarios y roles más complejos.
* Exponer una API REST utilizando un framework como Flask o FastAPI.
* Escribir pruebas unitarias para garantizar el correcto
  funcionamiento de los componentes.

## Licencia

Este proyecto se proporciona sin garantías como material didáctico. Puede
utilizarlo y modificarlo con fines educativos.