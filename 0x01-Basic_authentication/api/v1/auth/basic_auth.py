#!/usr/bin/env python3
'''Module implements the basicAuth class'''

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''Inherits from the Auth Class'''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''Returns the Base64 of the Authorization header'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header[len("Basic "):]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''Returns the decoded value of a Base64 str'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_base64 = base64.b64decode(base64_authorization_header)
            return decoded_base64.decode('utf-8')
        except Exception:
            return None
