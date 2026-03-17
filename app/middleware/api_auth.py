import os
from functools import wraps
from flask import request, jsonify
import secrets

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        master_key = os.getenv('API_KEY')
        if not master_key:
            return jsonify({'error': 'API key no configurada'}), 500
        if not api_key:
            return jsonify({'error': 'API key requerida'}), 401

        if not secrets.compare_digest(api_key, master_key):
            return jsonify({'error': 'API key inválida'}), 403

        return f(*args, **kwargs)

    return decorated