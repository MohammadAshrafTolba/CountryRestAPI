import unittest
import API.country_info
import json

class MyTestCase(unittest.TestCase):

    def test_get_info(self):
        C = API.country_info.CountryInfo()
        result = C.get_info("Egypt")
        self.assertTrue(len(result) > 0)

    def test_get_right_answer(self):
        C = API.country_info.CountryInfo()
        result = C.get_info("Egypt")
        info = result[0]["capital"]
        self.assertEqual(info , "Cairo")

    def test_wrong_name(self):
        C = API.country_info.CountryInfo()
        result = C.get_info("kiki")
        self.assertEqual(len(result),2)

if __name__ == '__main__':
    unittest.main()
