from flask import Blueprint, jsonify, request
from ..services.user_services import get_users_postgres_service, send_email_postgres_service
from loguru import logger
from .. import limiter
from ..middleware.api_auth import require_api_key

user_routes = Blueprint('user_routes', __name__, url_prefix='/api/users')

@user_routes.route('/', methods=['GET'])
@limiter.limit("10 per hour")
@require_api_key
def get_users():

    
    users = get_users_postgres_service() 
    
    return jsonify(users)

@user_routes.route('/send-email', methods=['POST'])
@limiter.limit("5 per hour")
@require_api_key
def send_email():
   

    data = request.get_json()

    if not data:
        return jsonify({'message': 'JSON body vacio'}), 400

    resultado = send_email_postgres_service(
        name=data.get('name', ''),
        lastname=data.get('lastname', ''),
        email=data.get('email', ''),
        company=data.get('company', ''),
        message=data.get('message', '')
    )
    
    return jsonify({'success': resultado}), 201

