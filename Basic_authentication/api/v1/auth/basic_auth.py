#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

import base64

from .auth import Auth


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
