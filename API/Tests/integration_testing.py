import unittest
import requests
from API.response_handler import ResponseHandler


class MyTestCase(unittest.TestCase):

    def test_empty_info(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/egypt?key='
        response = requests.get(url).json()
        self.assertEqual(response, self.handler.invalid_info)

    def test_valid_request(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/egypt?key=capital,name'
        response = requests.get(url).json()
        expected_data = {
            'capital': 'Cairo',
            'name': 'Egypt',
        }
        self.assertEqual(response, expected_data)

    def test_public_api_error(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/invalid_country?info=name'
        response = requests.get(url).json()
        self.assertEqual(response, self.handler.invalid_info)

    def test_invalid_request_wrong_info(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/egypt?key='
        response = requests.get(url).json()
        self.assertEqual(response, self.handler.invalid_info)

if __name__ == '__main__':
    unittest.main()