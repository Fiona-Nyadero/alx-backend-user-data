#!/usr/bin/env python3
'''Module obfuscates specified fields in log messages'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Returns the obfuscated log message'''
    for field in fields:
        hashing_info = f"{field}=[^{separator}]*"
        message = re.sub(hashing_info, f"{field}={redaction}", message)
    return message
