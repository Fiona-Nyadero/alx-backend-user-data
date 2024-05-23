#!/usr/bin/env python3
'''Module implements the Auth class'''
from flask import request
from typing import List, TypeVar


class Auth():
    '''Module for the Auth class'''
    def __init__(self):
        '''Initializes the class Auth'''
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Checks for authorization'''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Extracts Auth header from the request'''
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Returns authenticated user'''
        return None
