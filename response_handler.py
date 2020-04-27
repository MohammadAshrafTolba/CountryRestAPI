from country_info import CountryInfo


class ResponseHandler:

    def __init__(self):
        self.country_info = CountryInfo()
        self.keys = []
        self.invalid_info = {'error': 'keys field is empty or invalid'}
        self.public_api_error = {'error': 'public api error'}

    def get(self, name, keys):
        data = self.country_info.get_info(name)
        if data is None:
            return self.public_api_error
        response = self.filter(keys, data)
        return response

    def get_all_info(self, name):
        data = self.country_info.get_info(name)
        if data is None:
            return self.public_api_error
        return data

    def filter(self, keys, data):
        self.keys_list = keys.split(',')
        filtered_data = {}
        for i in self.keys_list:
            if i not in data:
                return self.invalid_info
            filtered_data[i] = data[i]
        return filtered_data