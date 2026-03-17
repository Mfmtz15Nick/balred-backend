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

Ejemplo de `.env`:

```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=cambia_esta_clave_por_una_segura
API_KEY=tu_api_key_aqui
DATABASE_URL=postgresql://usuario:password@host:5432/database
SMTP_GMAIL=tu_correo@gmail.com
SMTP_PASSWORD=tu_app_password
SMTP_TO_EMAIL=destinatario@tudominio.com
```

Variables necesarias para que arranque:
- `API_KEY`: obligatoria para consumir rutas protegidas.
- `DATABASE_URL`: obligatoria para consultas e inserciones en PostgreSQL.
- `SMTP_GMAIL` y `SMTP_PASSWORD`: obligatorias para enviar correos.
- `SMTP_TO_EMAIL`: opcional. Si no se define, se usa `SMTP_GMAIL` como destinatario.
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
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=cambia_esta_clave_por_una_segura
API_KEY=tu_api_key_aqui
DATABASE_URL=postgresql://usuario:password@host:5432/database
SMTP_GMAIL=tu_correo@gmail.com
SMTP_PASSWORD=tu_app_password
SMTP_TO_EMAIL=destinatario@tudominio.com
```

### 2. Levantar con Docker Compose

```bash
docker compose up --build
```

La API quedara disponible en:

```text
http://localhost:5000
```
