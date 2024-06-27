"""
    Flinks categorization entity
    ==============================

    This module defines the ``Categorization`` entity allowing to interact with the underlying API
    methods.
    Documentation: https://docs.flinks.com/reference/attributes

"""

from ..baseapi import BaseApi


class Categorization(BaseApi):
    """Wraps the categorization-related API methods."""

    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "categorization"

    def get_categorization(self, login_id: str, request_id: str):
        """Retrieves income attributes.

        :param login_id: valid login ID
        :param request_id: valid request ID
        :type login_id: str
        :type request_id: str
        :return: dictionary containing the transactions with categorization
        :rtype: dictionary

        """
        return self._client._call(
            "GET",
            self._build_path("login/" + login_id + "/requestid/" + request_id),
        )
