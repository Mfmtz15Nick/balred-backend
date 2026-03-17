from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import os

#Limiter configuration
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

def create_app():
    app = Flask(__name__)

    # Cors configuration
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    
    # Initialize limiter
    limiter.init_app(app)
    
    # Choose configuration based on environment variable
    env = os.getenv('FLASK_ENV', 'development')  # Default to 'development' if not set

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
    
    @app.errorhandler(429)
    def too_many_requests(error):
        return jsonify({'message': 'Too many requests'}), 429

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Internal Server Error: {error}')
        return jsonify({'message': 'Services is not available'}), 500

    # Optionally add URL rules if needed
    app.add_url_rule('/', endpoint='index', view_func=lambda: 'Welcome to the Flask API!')

    return app
