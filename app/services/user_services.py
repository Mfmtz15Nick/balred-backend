from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from app.database.postgresql import insert_prospecto, get_users_postgres
from loguru import logger


def get_users_postgres_service():
    try:
        users = get_users_postgres()
        
        return users
    except Exception as e:
        logger.error(f"Error al conectar a la base de datos: {e}")
        return []


    
def send_email_postgres_service(email, name, lastname, company, message):
    try:
        sender_email = os.getenv('SMTP_GMAIL')
        sender_password = os.getenv('SMTP_PASSWORD')
        recipient_email = os.getenv('SMTP_TO_EMAIL') or sender_email
        
        if not sender_email or not sender_password:
            raise ValueError("SMTP credentials not configured")
        if not recipient_email:
            raise ValueError("SMTP recipient not configured")


        subject = f"Solicitud de contacto de {name} {lastname} de parte de {company}"
        body = f"El usuario {name} {lastname} de la empresa {company} ha enviado el siguiente mensaje: \n\n{message}\n\nPuedes contactarlo en su correo: {email}"

        correo = MIMEMultipart()
        correo["From"] = sender_email
        correo["To"] = recipient_email
        correo["Subject"] = subject
        
        correo.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, correo.as_string())
        server.quit()
        
        insert_prospecto(name, lastname, email, company, message)
        
        return True
    except Exception as e:
        logger.error(f"Error al enviar el correo: {e}")
        return False


def login_service(data):
    return True
