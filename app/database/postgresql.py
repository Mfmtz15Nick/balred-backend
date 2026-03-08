import psycopg2
import os
from loguru import logger
from flask import abort


def connect_to_postgresql():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL') , sslmode='require')
        cursor = conn.cursor()
        if cursor:            logger.info("Conexión a la base de datos exitosa")
        
        return conn, cursor
    except Exception:
        logger.error(f"Error al conectar a la base de datos")
        return None, None
    
def insert_prospecto(name, lastname, email, company, message):
    if not validate_data(name, lastname, email, company, message):
        logger.warning("Intento de inserción con datos inválidos")
        abort(400, description="Datos inválidos: revisa los campos.")
    
    conn, cursor = None, None
    try:
        conn, cursor = connect_to_postgresql()
        if not cursor:
            abort(500, description="Error interno: conexión fallida.")
        
        query = "INSERT INTO prospectos (name, lastname, email, company, message) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, lastname, email, company, message))
        conn.commit()
        logger.info("Prospecto insertado exitosamente")
        return True

    except Exception:
        if conn: conn.rollback()
        logger.error(f"Error en BD")
        abort(500, description="Error al procesar la solicitud en la base de datos.")
        
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def get_users_postgres():
    conn, cursor = None, None
    try:
        conn, cursor = connect_to_postgresql()
        if not cursor: return []
        
        cursor.execute("SELECT name, lastname, email, company, message FROM prospectos") 
        users = cursor.fetchall()
        logger.info("Usuarios obtenidos exitosamente")
        return users
    
    except Exception:
        logger.error("Error al obtener usuarios")
        return []
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def validate_data(name, lastname, email, company, message):
    if not all([s.strip() for s in [name, lastname, email, company, message]]):
        return False

    if len(name) > 50 or len(lastname) > 50 or len(company) > 100 or len(message) > 2000:
        return False

    if "@" not in email or "." not in email.split("@")[-1]:
        return False
    
    return True