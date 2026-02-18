from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from requests import get
from flask import jsonify, current_app
import os


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


def get_user_by_id_service(id):
    user = get(f'https://randomuser.me/api')
    return user.json()

def send_email_service(email, name, lastName):
    try:
        sender_email = os.getenv('SMTP_GMAIL')
        sender_password = os.getenv('SMTP_PASSWORD')

        subject = "Hola"
        body = f"hola {name} {lastName}, khghjg"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
    
        db = current_app.config['MONGO_DB']
        users_collection = db['prospectos']
        users_collection.insert_one({"email": email, "name": name, "lastname": lastName})
        
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False
    

def login_service(data):
    return True