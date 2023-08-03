from functools import wraps
import secrets
from flask import request, jsonify
import decimal
import json

from models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        print('Headers:', request.headers)
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
            print(token)
        if not token:
            print('Token is missing')
            return jsonify({"message" : "Token is missing."}), 401
        
        print('Token:', token)

        try:
            current_user_token = User.query.filter_by(token=token).first()

        except:
            owner = User.query.filter_by(token=token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                print('Token is invalid')
                return jsonify({"message" : "Token is invalid"})
            
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)