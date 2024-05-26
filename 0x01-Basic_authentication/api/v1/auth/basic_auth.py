#!/usr/bin/env python3
'''Module implements the basicAuth class'''

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Inherits from the Auth Class'''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''Returns the Base64 of the Authorization header'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header[len("Basic "):]
        return None
