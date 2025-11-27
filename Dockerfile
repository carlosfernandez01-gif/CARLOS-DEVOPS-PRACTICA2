FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero las dependencias para aprovechar la cache de Docker
COPY requirements.txt /app/requirements.txt

# Instalamos dependencias (en este proyecto no hay externas, pero queda listo)
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . /app

# Evitamos buffer en la salida de Python (para ver bien los prints)
ENV PYTHONUNBUFFERED=1

# Comando por defecto: ejecutar el main de la tienda
CMD ["python", "main.py"]
