from flask import Blueprint, jsonify, request
from ..services.user_services import create_user_service, get_user_by_id_service, get_users_service, login_service, send_email_service
from loguru import logger

user_routes = Blueprint('user_routes', __name__, url_prefix='/api/users')

@user_routes.route('/', methods=['GET'])
def get_users():
    logger.debug('Enter get_users() ')
    
    users = get_users_service() 
    
    return users

@user_routes.route('/sendEmail', methods=['POST'])
def send_email():
    logger.debug('Enter send_email()')

    data = request.get_json()

    if not data:
        return jsonify({'message': 'JSON body vacio'}), 400

    email = data.get('email')
    name = data.get('name')
    lastName = data.get('lastName')

    if not email:
        return jsonify({'success': False}), 400

    resultado =send_email_service(email, name, lastName)
    
    return jsonify({'success': resultado}), 200 if resultado else 500

