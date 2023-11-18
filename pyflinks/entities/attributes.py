"""
    Flinks attributes entity
    ==============================

    This module defines the ``Attributes`` entity allowing to interact with the underlying API
    methods.
    Documentation: https://docs.flinks.com/reference/attributes

"""

from ..baseapi import BaseApi


class Attributes(BaseApi):
    """Wraps the banking services-related API methods."""

    def __init__(self, client):
        super().__init__(client)
        self.endpoint = "insight"

    def get_lending_attributes(self, login_id: str, request_id: str):
        """Retrieves lending attributes.

        :param login_id: valid login ID
        :param request_id: valid request ID
        :type login_id: str
        :type request_id: str
        :return: dictionary containing the lending attributes
        :rtype: dictionary

        """
        return self._client._call(
            "GET",
            self._build_path(
                "login/"
                + login_id
                + "/attributes/"
                + request_id
                + "/GetLendingAttributes"
            ),
        )

    def get_income_attributes(self, login_id: str, request_id: str):
        """Retrieves income attributes.

        :param login_id: valid login ID
        :param request_id: valid request ID
        :type login_id: str
        :type request_id: str
        :return: dictionary containing the income attributes
        :rtype: dictionary

        """
        return self._client._call(
            "GET",
            self._build_path(
                "login/"
                + login_id
                + "/attributes/"
                + request_id
                + "/GetIncomeAttributes"
            ),
        )
