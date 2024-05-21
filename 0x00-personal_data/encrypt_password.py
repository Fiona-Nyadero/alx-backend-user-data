#!/usr/bin/env python3
'''Module encrypts and checks for valid passwords'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Fx returns a salted and hashed password'''
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Fx checks for valid passwords'''
    valid_p = bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return valid_p
