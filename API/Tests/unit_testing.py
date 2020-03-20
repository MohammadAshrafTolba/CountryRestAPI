import unittest
import json
from API.response_handler import ResponseHandler
from API.country_info import CountryInfo


class CountryInfoPlaceHolder:       #   To make tests available offline
    def __init__(self, input):
        self.input = input
    def get_info(self, name):
        return self.input

class MyTestCase(unittest.TestCase):


        #   Testing the get_info(name, info) function


    def test_get_any_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get_all_info('egypt')
        self.assertTrue(len(response) > 0)

    def test_invalid_keys(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt', 'namee')
        self.assertEqual(response, handler.invalid_info)

    def test_get_true_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt', 'name')
        self.assertEqual(response['name'], 'Egypt')

    def test_empty_keys(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt','')
        self.assertEqual(response, handler.invalid_info)

    def test_public_api_error_get(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder(None)
        response = handler.get('egypt', 'capital')
        self.assertEqual(response, handler.public_api_error)

    def test_get_valid_data(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"capital": "Cairo", "demonym": "Egyptian"})
        response = handler.get('egypt', 'capital+demonym')
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)


        #   Testing the get_info(name) function in the CountryInfo class
        #   Require internet connection


    def test_get_invalid_country(self):
        country_info = CountryInfo()
        response = country_info.get_info('zzzzz')
        self.assertEqual(response, None)


if __name__ == '__main__':
    unittest.main()
