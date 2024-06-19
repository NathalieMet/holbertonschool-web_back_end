#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

from .auth import Auth


class BasicAuth(Auth):
    """ Class to manage the API authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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
