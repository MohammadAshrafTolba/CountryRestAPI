from response_handler import ResponseHandler
from flask_restful import Resource
import json

class OfflineCountryInfo:

    def get_info(self, name):
        if name.lower() != 'egypt':
            return None
        egypt_info = self.get_egypt_info()
        return egypt_info

    def get_egypt_info(self):
        with open('offline_country_info.json', 'r') as file:
            egypt_info = json.load(file)
        return egypt_info

class OfflineResponseHandler(Resource, ResponseHandler):

    def __init__(self):
        super().__init__()
        self.country_info = OfflineCountryInfo()

    def get(self, name, keys):
        self.offline_data = self.country_info.get_info(name)
        if self.offline_data is None:
            return self.public_api_error
        response = self.filter(keys, self.offline_data)
        return response

    def get_all_info(self, name):
        self.offline_data = self.country_info.get_info(name)
        if self.offline_data is None:
            return self.public_api_error
        return self.offline_data

    def filter(self, keys, data):
        self.keys_list = keys.split(',')
        filtered_data = {}
        for i in self.keys_list:
            if i not in data:
                return self.invalid_info
            filtered_data[i] = data[i]
        return filtered_data