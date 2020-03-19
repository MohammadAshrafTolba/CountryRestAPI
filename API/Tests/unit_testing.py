import unittest
from API.response_handler import ResponseHandler

class CountryInfoPlaceHolder:       #   To make tests available offline
    def __init__(self, input):
        self.input = input
    def get_info(self, name):
        return self.input

class FakeParse:
    def __init__(self, input):
        self.input = input
    def parse_args(self):     #   To override the original request parser functions
        return self.input


class MyTestCase(unittest.TestCase):


        #   Testing the get_info(name, info) function


    def test_get_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get_info('egypt', 'all')
        self.assertTrue(len(response) > 0)

    def test_invalid_info_get_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get_info('egypt', ['namee'])
        self.assertEqual(response, handler.invalid_info)

    def test_true_info_get_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get_info('egypt', ['name'])
        self.assertEqual(response['name'], 'Egypt')

    def test_empty_info_get_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get_info('egypt',[''])
        self.assertEqual(response, handler.invalid_info)

    def test_public_api_error_get_info(self):
        handler = ResponseHandler()
        fake_info = CountryInfoPlaceHolder(None)
        handler.country_info = fake_info
        response = handler.get_info('egypt', ['capital'])
        self.assertEqual(response, handler.public_api_error)

    def test_valid_data_get_info(self):
        handler = ResponseHandler()
        handler.country_info = CountryInfoPlaceHolder({"capital": "Cairo", "demonym": "Egyptian"})
        response = handler.get_info('egypt', ['capital', 'demonym'])
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)


            #   Testing the get(name) fuction

    def test_invalid_info_get(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': 'namee'})
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt')
        self.assertEqual(response, handler.invalid_info)

    def test_get_info_2(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': 'all'})
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt')
        self.assertTrue(len(response) > 0)

    def test_true_info_get(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': 'name'})
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt')
        self.assertEqual(response['name'], 'Egypt')

    def test_empty_info_get(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': ''})
        handler.country_info = CountryInfoPlaceHolder({"name": "Egypt", "capital":"Cairo"})
        response = handler.get('egypt')
        self.assertEqual(response, handler.invalid_info)

    def test_public_api_error_get(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': 'capital'})
        handler.country_info = CountryInfoPlaceHolder(None)
        response = handler.get('egypt')
        self.assertEqual(response, handler.public_api_error)

    def test_valid_data_get(self):
        handler = ResponseHandler()
        handler.parser = FakeParse({'key': 'capital,demonym'})
        handler.country_info = CountryInfoPlaceHolder({"capital": "Cairo", "demonym": "Egyptian"})
        response = handler.get('egypt')
        expected = {"capital": "Cairo", "demonym": "Egyptian"}
        self.assertEqual(expected, response)



if __name__ == '__main__':
    unittest.main()
