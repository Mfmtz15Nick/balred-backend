from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .database.mongo import ping_mongo, create_mongo_client
import os


def create_app():
    app = Flask(__name__)

    print('Creando create_app()')

    # Configurations
    # app.config.from_object('app.config.Config')  # Assuming you have a config.py with Config class

    # Choose configuration based on environment variable
    env = os.getenv('FLASK_ENV', 'development')  # Default to 'development' if not set

    # if env == 'production':
    #     app.config.from_object('app.config.ProductionConfig')
    # else:
    #     app.config.from_object('app.config.DevelopmentConfig')

    # Database configuration
    # mongo_client = create_mongo_client()
    
    # if not ping_mongo():
        #raise RuntimeError('Failed to connect to MongoDB')
    #else:
        #print('Mongo was connected! :D ')
    
    #app.config['MONGO_CLIENT'] = mongo_client
    #app.config['MONGO_DB'] = mongo_client.get_db()

    # Routes
    from .routes.user_routes import user_routes
    app.register_blueprint(user_routes)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'message': 'Resource not found'}), 404
    
    @app.errorhandler(405)
    def not_found_error(error):
        return jsonify({'message': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Internal Server Error: {error}')
        return jsonify({'message': 'Services is not available'}), 500

    # Optionally add URL rules if needed
    app.add_url_rule('/', endpoint='index', view_func=lambda: 'Welcome to the Flask API!')

    return app
