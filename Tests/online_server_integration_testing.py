import unittest2
from response_handler import ResponseHandler
from server import app

class MyTestCase(unittest2.TestCase):


    def test_valid_request(self):
        url = '/country/name/egypt/keys/capital,name'
        testClient = app.test_client()
        testClient.testing = True
        response = testClient.get(url)
        expected_data = {
            'capital': 'Cairo',
            'name': 'Egypt',
        }
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_data)

    def test_public_api_error(self):
        self.handler = ResponseHandler()
        url = '/country/name/invalid_country/keys/name'
        testClient = app.test_client()
        testClient.testing = True
        response = testClient.get(url)
        self.assertEqual(response.json, self.handler.public_api_error)

    def test_invalid_request_wrong_info(self):
        self.handler = ResponseHandler()
        url = '/country/name/egypt/keys/invalid_key'
        testClient = app.test_client()
        testClient.testing = True
        response = testClient.get(url)
        self.assertEqual(response.json, self.handler.invalid_info)

if __name__ == '__main__':
    unittest2.main()