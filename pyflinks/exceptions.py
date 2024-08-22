"""
    Flinks client exceptions
    ========================

    This module defines top-level exceptions that can be used by the Flinks client implementation.

"""


from typing import Any, Optional
import requests


class FlinksError(Exception):
    """Base exception for all exceptions that can be raised by the Flinks client."""

    def __init__(self, msg: str, response: requests.Response):
        self.msg = msg
        self.response = response

    def __str__(self):
        return self.msg or super().__str__()


class TransportError(FlinksError):
    """Raised when an error occurs related to the connection with the Flinks service."""

    def __init__(self, msg: str, response: requests.Response):
        super().__init__(msg, response)


class ProtocolError(FlinksError):
    """Raised when an error occurs related to the response processing."""

    def __init__(
        self, msg: str, response=requests.Response, data: Optional[Any] = None
    ):
        super().__init__(msg, response)
        self.data = data
