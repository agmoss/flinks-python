"""
    Flinks client
    =============

    This module defines the ``Client`` class allowing to interact with the Flinks API endpoints and
    methods.
    Documentation: https://sandbox.flinks.io/documentation/

"""

from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError

from .entities.attributes import Attributes
from .entities.banking_services import BankingServices
from .entities.categorization import Categorization
from .exceptions import ProtocolError, TransportError


class Client:
    """The Flinks API client class."""

    def __init__(
        self,
        customer_id: str,
        base_url: Optional[str] = None,
        http_max_retries: Optional[int] = None,
    ):
        """Initializes the Flinks client.

        :param customer_id: authorization key required to interact with the API endpoints
        :param base_url: base URL of the API endpont (eg. "https://sandbox.flinks.io/v3/")
        :param http_max_retries: maximum number of retries each connection should attempt
        :type customer_id: str
        :type base_url: str
        :type http_max_retries: int
        :return: :class:`Client <Client>` object
        :rtype: flinks.client.Client

        """
        # Initializes attributes related to the client settings.
        self.api_endpoint = (
            urljoin(base_url or "https://sandbox.flinks.io/v3/", customer_id) + "/"
        )
        self.session = requests.Session()
        self.session.mount(
            self.api_endpoint, HTTPAdapter(max_retries=http_max_retries or 3)
        )

        # Set up entities.
        self._banking_services: Optional[BankingServices] = None
        self._attributes: Optional[Attributes] = None
        self._categorization: Optional[Categorization] = None

        ###################
        # FLINKS ENTITIES #
        ###################

    @property
    def banking_services(self) -> BankingServices:
        """Allows to access the banking services entity.

        :return: :class:`BankingServices <BankingServices>` object
        :rtype: flinks.entities.banking_services.BankingServices

        """
        if self._banking_services is None:
            from .entities.banking_services import BankingServices

            self._banking_services = BankingServices(self)
        return self._banking_services

    @property
    def attributes(self) -> Attributes:
        """Allows to access the attributes entity.

        :return: :class:`Attributes <Attributes>` object
        :rtype: flinks.entities.attributes.Attributes

        """
        if self._attributes is None:
            from .entities.attributes import Attributes

            self._attributes = Attributes(self)
        return self._attributes

    @property
    def categorization(self) -> Categorization:
        """Allows to access the categorization entity.

        :return: :class:`Categorization <Categorization>` object
        :rtype: flinks.entities.categorization.Categorization

        """
        if self._categorization is None:
            from .entities.categorization import Categorization

            self._categorization = Categorization(self)
        return self._categorization

        ##################################
        # PRIVATE METHODS AND PROPERTIES #
        ##################################

    def _call(
        self,
        http_method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Calls the API endpoint."""
        # Prepares the headers and parameters that will be used to forge the request.
        headers = {"cache-control": "no-cache", "Content-Type": "application/json"}
        params = params or {}

        # Calls the API endpoint!
        request = getattr(self.session, http_method.lower())
        try:
            response = request(
                urljoin(self.api_endpoint, path),
                headers=headers,
                params=params,
                json=data,
            )
            response.raise_for_status()
        except HTTPError:
            if response.status_code != 400:
                raise TransportError(
                    "Got unsuccessful response from server (status code: {})".format(
                        response.status_code,
                    ),
                    response=response,
                )

        # Ensures the response body can be deserialized to JSON.
        try:
            response_data = response.json()
        except ValueError as e:
            raise ProtocolError(
                "Unable to deserialize response body: {}".format(e),
                response=response,
            )

        # Properly handles potential errors.
        if response.status_code > 299 and response_data.get("FlinksCode"):
            raise ProtocolError(
                response_data.get("FlinksCode") or "FLINKS_ERROR",
                response=response,
                data=response_data,
            )

        return response_data
