#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth():
    """ Class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ function require_auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ function authorization_header
        """
        return None

    def current_user(self, request=None) -> User:
        """ function current_user
        """
        return None
