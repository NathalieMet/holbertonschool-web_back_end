#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
from db import DB
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
      - JSON payload of the form:
        {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """ POST /users/
    JSON body:
      - email
      - password
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login_user() -> str:
    """ POST /sessions/
    Form data:
      - email
      - password
    Return:
      - JSON payload of the form:
        {"email": "<user email>", "message": "logged in"}
      - 401 if login information is incorrect
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout_user() -> str:
    """ DELETE /sessions/
    Removes the user session
    """
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    response = make_response(redirect('/'))
    response.delete_cookie('session_id')
    return response


@app.route('/profile', methods=['GET'], strict_slashes=False)
def get_profile() -> str:
    """ GET /profile/
    The request is expected to contain a session_id cookie. Use it to find the
    user. If the user exist, respond with a 200 HTTP status and the following
    JSON payload:
    {"email": "<user email>"}
    """
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ POST /reset_password/
    If the email is not registered, respond with a 403 status code. Otherwise,
    generate a token and respond with a 200 HTTP status and the following JSON
    payload:
    {"email": "<user email>", "reset_token": "<reset token>"}
    """
    email = request.form.get('email')

    if email is None:
        abort(403)

    try:
        new_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": new_token}), 200

    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ POST /reset_password/
    If the email is not registered, respond with a 403 status code. Otherwise,
    generate a token and respond with a 200 HTTP status and the following JSON
    payload:
    {"email": "<user email>", "reset_token": "<reset token>"}
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if not reset_token or not new_password:
        abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200

    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
