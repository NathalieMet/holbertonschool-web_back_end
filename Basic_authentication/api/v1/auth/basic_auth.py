#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

import base64

from .auth import Auth
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Class to manage the API authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header for a Basic
        Authentication
    """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]
            else:
                return authorization_header[5:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ returns the decoded value of a Base64 string
        base64_authorization_header:
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            if len(base64_authorization_header) % 4 != 0:
                return None
            decoded_value = base64.b64decode(base64_authorization_header,
                                             validate=True).decode('utf-8')
            return decoded_value
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        separator = decoded_base64_authorization_header.find(":")
        email = decoded_base64_authorization_header[:separator]
        password = decoded_base64_authorization_header[separator + 1:]

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if not users or len(users) == 0:
            return None

        user: User = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request
        """
        authorization = self.authorization_header(request)
        if authorization is None:
            return None

        extracted = self.extract_base64_authorization_header(authorization)
        if extracted is None:
            return None

        decoded = self.decode_base64_authorization_header(extracted)
        if decoded is None:
            return None

        email, password = self.extract_user_credentials(decoded)
        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)
        return user
