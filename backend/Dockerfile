# Usar una imagen oficial de Python como base
FROM python:3.12.3-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios para instalar dependencias
COPY backend/requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código de la aplicación Django
COPY backend/ /app/

# Exponer el puerto que Django usará
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
