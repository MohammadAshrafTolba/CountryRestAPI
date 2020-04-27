import unittest2
import json
from response_handler import ResponseHandler
from country_info import CountryInfo

class CountryInfoPlaceHolder:       #   To make tests available offline
    def __init__(self, input):
        self.input = input
    def get_info(self, name):
        return self.input

class MyTestCase(unittest2.TestCase):


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
        response = handler.get('egypt', 'capital,demonym')
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)


        #   Testing the filter(keys, data) function

    def test_filter_with_valid_keys(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"capital": "Cairo", "demonym": "Egyptian"})
        with open('offline_country_info.json') as file:
            info = json.load(file)
        response = handler.filter('capital,demonym', info)
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)

    def test_filter_with_invalid_keys(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"capital": "Cairo", "demonym": "Egyptian"})
        with open('offline_country_info.json') as file:
            info = json.load(file)
        response = handler.filter('capital,invalid_key', info)
        self.assertEqual(handler.invalid_info, response)


        #   Testing the get_info(name) function in the CountryInfo class
        #   Require internet connection


    def test_get_invalid_country(self):
        country_info = CountryInfo()
        response = country_info.get_info('zzzzz')
        self.assertEqual(response, None)


if __name__ == '__main__':
    unittest2.main()
