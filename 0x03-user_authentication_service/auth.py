#!/usr/bin/env python3
""" Module for Auth"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
