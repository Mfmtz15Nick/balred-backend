from flask import Blueprint, jsonify, request
from ..services.user_services import create_user_service, get_user_by_id_service, get_users_service, login_service
from loguru import logger

user_routes = Blueprint('user_routes', __name__, url_prefix='/api/users')

@user_routes.route('/', methods=['GET'])
def get_users():
    logger.debug('Enter get_users() ')
    
    users = get_users_service() 
    
    return users