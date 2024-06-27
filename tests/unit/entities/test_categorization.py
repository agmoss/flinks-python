import unittest.mock

from pyflinks import Client


class TestBankingServices:
    @unittest.mock.patch('requests.Session.get')
    def test_can_initiate_get_categorization(self, mocked_get):
        mocked_response = unittest.mock.Mock(status_code=200, content='{}')
        mocked_response.json.return_value = {'Result': '', }
        mocked_get.return_value = mocked_response

        client = Client('foo-12345', 'https://username.flinks-custom.io')
        client.categorization.get_categorization('login-1234', 'request-1234')

        assert (
            mocked_get.call_args[0][0] ==
            (
                'https://username.flinks-custom.io/foo-12345/categorization/'
                'login/login-1234/requestid/request-1234'
            )
        )
