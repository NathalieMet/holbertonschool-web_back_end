#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""

import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "password", "phone", "ssn")

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.

        Args:
            fields (List[str]): The fields to obfuscate in the log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with sensitive fields redacted.
        """
        original_message = super(RedactingFormatter, self).format(record)
        redacted_message = filter_datum(self.fields, self.REDACTION,
                                        original_message, self.SEPARATOR)
        return redacted_message


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Write a function called filter_datum that returns the log message
    obfuscated:
Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields
in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the
substitution with a single regex.
"""
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}",
                  message)

def get_logger() -> logging.Logger:
    """Creates and returns a logger object configured with RedactingFormatter.

    Returns:
        logging.Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create console handler and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create and add formatter to the handler
    formatter = RedactingFormatter(list(PII_FIELDS))
    ch.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(ch)

    return logger

if __name__ == "__main__":
    logger = get_logger()
