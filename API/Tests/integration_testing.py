import unittest2
import requests
from API.response_handler import ResponseHandler


class MyTestCase(unittest2.TestCase):

    def test_valid_request(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/egypt/keys/capital,name'
        response = requests.get(url).json()
        expected_data = {
            'capital': 'Cairo',
            'name': 'Egypt',
        }
        self.assertEqual(response, expected_data)

    def test_public_api_error(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/invalid_country/keys/name'
        response = requests.get(url).json()
        self.assertEqual(response, self.handler.public_api_error)

    def test_invalid_request_wrong_info(self):
        self.handler = ResponseHandler()
        url = 'http://localhost:5000/country/name/egypt/keys/invalid_key'
        response = requests.get(url).json()
        self.assertEqual(response, self.handler.invalid_info)

if __name__ == '__main__':
    unittest2.main()