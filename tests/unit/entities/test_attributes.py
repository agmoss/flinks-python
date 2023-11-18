import unittest.mock

from pyflinks import Client


class TestBankingServices:
    @unittest.mock.patch('requests.Session.get')
    def test_can_initiate_get_income_attributes(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {'Result': '', }
        mocked_get.return_value = mocked_response

        client = Client('foo-12345', 'https://username.flinks-custom.io')
        client.attributes.get_income_attributes( 'login-1234', 'request-1234')

        assert (
            mocked_get.call_args[0][0] ==
            (
                'https://username.flinks-custom.io/foo-12345/insight/'
                'login/login-1234/attributes/request-1234/GetIncomeAttributes'
            )
        )


    @unittest.mock.patch('requests.Session.get')
    def test_can_initiate_get_lending_attributes(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {'Result': '', }
        mocked_get.return_value = mocked_response

        client = Client('foo-12345', 'https://username.flinks-custom.io')
        client.attributes.get_lending_attributes( 'login-1234', 'request-1234')

        assert (
            mocked_get.call_args[0][0] ==
            (
                'https://username.flinks-custom.io/foo-12345/insight/'
                'login/login-1234/attributes/request-1234/GetLendingAttributes'
            )
        )
