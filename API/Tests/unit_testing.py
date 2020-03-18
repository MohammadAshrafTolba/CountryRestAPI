import unittest
from API.response_handler import ResponseHandler
from flask_restful import reqparse

class CountryPlaceHolder:
    def __init__(self, input):
        self.input = input
    def get_info(self, name):
        return self.input

class MyTestCase(unittest.TestCase):


        #   Testing the get_info(name, info) function


    def test_get_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt', 'all')
        self.assertTrue(len(response) > 0)

    def test_invalid_info_get_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt', ['capetal'])
        self.assertEqual(response, self.handler.invalid_info)

    def test_true_info_get_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt', ['capital'])
        self.assertEqual(response['capital'], 'Cairo')

    def test_empty_info_get_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt',[''])
        self.assertEqual(response, self.handler.invalid_info)

    def test_public_api_error_get_info(self):
        self.handler = ResponseHandler()
        fake_info = CountryPlaceHolder(None)
        self.handler.country_info = fake_info
        response = self.handler.get_info_from_public_api('egypt', ['capital'])
        self.assertEqual(response, self.handler.public_api_error)

    def test_get_info_invalid_data_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt', ['blablabla'])
        self.assertEqual(response, self.handler.invalid_info)

    def test_get_info_valid_data_info(self):
        self.handler = ResponseHandler()
        response = self.handler.get_info_from_public_api('egypt', ['capital', 'demonym'])
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)


if __name__ == '__main__':
    unittest.main()
