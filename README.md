# Balred Backend (Heatmap Project)

Backend construido con **Flask** y **MongoDB** para la gestion de prospectos y mapas de calor del proyecto Balred.

## Requisitos Previos

* Python 3.9 o superior.
* Acceso a un cluster de MongoDB Atlas.
* Git instalado.

## Guia de Instalacion

Sigue estos pasos para configurar el proyecto en tu maquina local:

### 1. Clonar el repositorio
Descarga el codigo fuente a tu maquina:
```bash
git clone https://github.com/Mfmtz15Nick/balred-backend.git
cd balred-backend
```

### 2. Crear entorno virtual
Crea un entorno virtual para tu proyecto:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Variables de entorno

```bash
cp .env.example .env
```

Ejemplo minimo de `.env`:

```env
# Requerida: conexion a MongoDB Atlas
MONGO_URI=mongodb+srv://usuario:password@cluster0.ejemplo.mongodb.net/balred?retryWrites=true&w=majority

# Recomendadas
FLASK_ENV=development
FLASK_APP=app
SECRET_KEY=cambia_esta_clave_por_una_segura
```

Variables necesarias para que arranque:
- `MONGO_URI`: obligatoria. Sin esta variable la app no puede conectarse a MongoDB.
- `FLASK_ENV`, `FLASK_APP`, `SECRET_KEY`: recomendadas para entorno local y configuracion general.

### 5. Correr proyecto

```bash
flask run
```

## Docker

### 1. Crear archivo de variables de entorno

```bash
cp .env.example .env
```

Usa este ejemplo en `.env` antes de levantar Docker:

```env
MONGO_URI=mongodb+srv://usuario:password@cluster0.ejemplo.mongodb.net/balred?retryWrites=true&w=majority
FLASK_ENV=development
FLASK_APP=app
SECRET_KEY=cambia_esta_clave_por_una_segura
```

### 2. Levantar con Docker Compose

```bash
docker compose up --build
```

La API quedara disponible en:

```text
http://localhost:5000
```
