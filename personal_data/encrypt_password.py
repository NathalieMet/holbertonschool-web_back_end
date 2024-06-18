#!/usr/bin/env python3
"""
Implement a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Implement a hash_password function that expects one string argument
    name password and returns a salted, hashed password, which is a byte
    string.
        """
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Implement an is_valid function that expects 2 arguments and returns
    a boolean.
    """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
