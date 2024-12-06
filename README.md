# Simple Recruiting Assignment  

Este proyecto consiste en una aplicación dividida en dos partes: un **frontend en Angular con Ionic** y un **backend en Django**. La comunicación entre ambos se realiza mediante **WebSockets**, y los mensajes enviados son almacenados en una base de datos **PostgreSQL** alojada en la nube.

---

# Requisitos Previos  

### 1. Frontend  
- Node.js (v16 o superior).  
- Angular y Ionic CLI instalado globalmente: 
  ```bash
  npm install -g @angular/cli
  npm install -g @ionic/cli
  ```

### 2. Backend  
- Docker y Docker Compose instalados.  
- Python 3.9+ (para desarrollo local del backend). 
  
### 3. Base de Datos  
- Asegúrate de tener acceso a las credenciales de la base de datos PostgreSQL alojada en la nube.  

### 4. Configuración de Redis  
-  Redis se ejecuta como un contenedor Docker incluido en `docker-compose.yml`.

  

# Instalación y Ejecución

### 1. Clonar el Repositorio  
Primero, clona el repositorio en tu máquina local:
```bash
  git clone <URL_DEL_REPOSITORIO>
  cd <NOMBRE_DEL_PROYECTO>
````


### 2. Backend (Django)
#### a. Variable de Entorno
- Crea un archivo .env en la carpeta del backend con las siguientes configuraciones: 
  ```bash
  SECRET_KEY='clave-secreta-django' 
  DEBUG=True 
  ALLOWED_HOSTS=*
  DATABASE_URL='postgres://usuario:contraseña@host:puerto/nombre_base_datos'
  REDIS_URL='redis://redis:6379/0' (Puerto 6380 en mi caso) 

#### b. Construcción y Ejecución con Docker Compose
```bash
docker-compose up --build
```
- Esto iniciará los contenedores de Redis y el backend de Django.

#### c. Migraciones de Base de Datos
- Ejecuta las migraciones: <br>
```bash 
docker exec -it <nombre_contenedor_backend> python manage.py migrate
```

#### d. Comprobación
- El backend estará disponible en http://localhost:8000.


### 3. Frontend (Angular)
#### a. Instalación de Dependencias
- Desde la carpeta frontend, ejecuta:
```bash
  npm install
```
#### b. Configuración del Endpoint de WebSocket
- Actualiza el archivo `chat.service.ts` para que coincida con la URL del backend:
  ```bash
  this.socket$ = new WebSocketSubject('ws://localhost:8000/ws/chat/'); // Cambiar según la URL del backend
  ```

#### c. Ejecución
```bash
  ionic serve
```
- El frontend estará disponible en http://localhost:8100
