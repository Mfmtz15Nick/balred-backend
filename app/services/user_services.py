from requests import get
from flask import jsonify, current_app


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

def login_service(data):
    return True