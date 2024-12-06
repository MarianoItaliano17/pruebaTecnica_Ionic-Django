# Usar una imagen base oficial de Python
FROM python:3.12.3-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app/

# Exponer el puerto para Daphne (ASGI server)
EXPOSE 8000

# Comando por defecto para ejecutar el servidor ASGI
CMD ["daphne", "backend.asgi:application"]
