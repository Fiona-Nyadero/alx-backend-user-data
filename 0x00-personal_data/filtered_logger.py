#!/usr/bin/env python3
'''Module obfuscates specified fields in log messages'''
from typing import List
import logging
import mysql.connector
import os
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Returns the obfuscated log message'''
    for field in fields:
        hashing_info = f"{field}=[^{separator}]*"
        message = re.sub(hashing_info, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''Initializes the class RedactingFormatter'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Filters values from incoming logs'''
        message = super().format(record)

        formatted_logg = filter_datum(self.fields, self.REDACTION,
                                      message, self.SEPARATOR)
        return formatted_logg


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """doc doc doc"""
    curr_logger = logging.getLogger("user_data")
    curr_logger.setLevel(logging.INFO)
    curr_logger.propagate = False
    streamhndlr = logging.StreamHandler()
    streamhndlr.setFormatter(RedactingFormatter(PII_FIELDS))
    curr_logger.addHandler(sh)
    return curr_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Retrieves database credentials'''
    user_name = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    pass_word = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    local_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    data_base = os.getenv("PERSONAL_DATA_DB_NAME")
    db_cred = mysql.connector.connect(user=user_name, password=pass_word,
                                      host=local_host, database=data_base)
    return db_cred
