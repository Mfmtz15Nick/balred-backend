from flask import jsonify

def success_response(data=None, status='Completed', message="Operation completed successfully"):
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return jsonify(response), 200

def error_response(message="An error occurred", status_code=500, details=None):
    response = {
        "status": "error",
        "message": message,
        "details": details
    }
    return jsonify(response), status_code
