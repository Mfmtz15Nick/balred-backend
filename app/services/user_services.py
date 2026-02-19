from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from requests import get
from flask import jsonify, current_app
import os
import psycopg2


def create_user_service(data):
        # Insert the document
    data = { "id":1, "name": "Mario", "lastname": "Fonseca", "mail": 'mfmtz@gmail.com', 'password': '123' }
    return data

def get_users_service():
    db = current_app.config['MONGO_DB']
    users_collection = db['prospectos']   

    users = list(users_collection.find())

    for user in users:
        user['_id'] = str(user['_id'])

    return jsonify(users)

def get_users_postgres_service():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL') , sslmode='require')
        cursor = conn.cursor()
        if cursor:            print("Conexión a la base de datos exitosa")
        
        cursor.execute("SELECT name, lastname, email, company, message FROM prospectos")
        users = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return users
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []


def get_user_by_id_service(id):
    user = get(f'https://randomuser.me/api')
    return user.json()

def send_email_service(email, name, lastName, company, message):
    try:
        sender_email = os.getenv('SMTP_GMAIL')
        sender_password = os.getenv('SMTP_PASSWORD')
        
        if not sender_email or not sender_password:
            raise ValueError("SMTP credentials not configured")


        subject = "Hola"
        body = f"hola {name} {lastName}, {message}"

        correo = MIMEMultipart()
        correo["From"] = sender_email
        correo["To"] = email
        correo["Subject"] = subject

        correo.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, correo.as_string())
        server.quit()
    
        db = current_app.config['MONGO_DB']
        users_collection = db['prospectos']
        users_collection.insert_one({"email": email, "name": name, "lastname": lastName, "company": company, "message": message})
        
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False
    
def send_email_postgres_service(email, name, lastname, company, message):
    try:
        sender_email = os.getenv('SMTP_GMAIL')
        sender_password = os.getenv('SMTP_PASSWORD')
        
        if not sender_email or not sender_password:
            raise ValueError("SMTP credentials not configured")


        subject = "Hola"
        body = f"hola {name} {lastname}, {message}"

        correo = MIMEMultipart()
        correo["From"] = sender_email
        correo["To"] = email
        correo["Subject"] = subject
        
        correo.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, correo.as_string())
        server.quit()
        
        conn = psycopg2.connect(os.getenv('DATABASE_URL') , sslmode='require')
        cursor = conn.cursor()
        if cursor:            print("Conexión a la base de datos exitosa")
        
        insert_query = """
        INSERT INTO prospectos (name, lastName, email, company, message)
        VALUES (%s, %s, %s, %s, %s) 
        """
        cursor.execute(insert_query, (name, lastname, email, company, message))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        return False


def login_service(data):
    return True