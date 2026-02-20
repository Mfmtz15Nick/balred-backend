# Balred Backend (Heatmap Project)

Backend construido con **Flask** y **MongoDB** para la gestión de prospectos y mapas de calor del proyecto Balred.

## 📋 Requisitos Previos

* Python 3.9 o superior.
* Acceso a un clúster de MongoDB Atlas.
* Git instalado.

## 🛠️ Guía de Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

### 1. Clonar el repositorio
Descarga el código fuente a tu máquina:
```bash
git clone [https://github.com/Mfmtz15Nick/balred-backend.git](https://github.com/Mfmtz15Nick/balred-backend.git)
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

### 5. Correr proyecto

```bash
flask run
```
## Docker

### 1. Crear archivo de variables de entorno

```bash
cp .env.example .env
```

### 2. Levantar con Docker Compose

```bash
docker compose up --build
```

La API quedar� disponible en:

```text
http://localhost:5000
```
