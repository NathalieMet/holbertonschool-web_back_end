#!/usr/bin/env python3
"""
Session_auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """ POST /auth_session/login
    Return:
      - dictionary representation of the User
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_logout():
    """ DELETE /auth_session/login
    Return:
      empty dictionnary
    """
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)

    return jsonify({}), 200
