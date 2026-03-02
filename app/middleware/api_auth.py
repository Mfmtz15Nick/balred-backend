import os
from functools import wraps
from flask import request, jsonify

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        print(f"API Key recibida: {api_key}")
        print(f"API Key esperada: {os.getenv('API_KEY')}")

        if not api_key:
            return jsonify({'error': 'API key requerida'}), 401

        if api_key != os.getenv('API_KEY'):
            return jsonify({'error': 'API key inválida'}), 403

        return f(*args, **kwargs)

    return decorated