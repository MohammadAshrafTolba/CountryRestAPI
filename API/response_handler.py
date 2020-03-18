from flask_restful import Resource, reqparse
from API.country_info import CountryInfo

class ResponseHandler(Resource):

    def __init__(self):

        self.country_info = CountryInfo()

        # defining keys in the url

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('key')

        # specifying error messages

        self.invalid_info = {'message': 'specification field is empty or invalid'}
        self.public_api_error = {'message': 'public api is not reachable'}

    def get(self, name):
        arguments = self.parser.parse_args()
        if arguments['key'] is None:
            return self.invalid_info
        info = arguments['key'].split(',')
        resp = self.get_info_from_public_api(name, info)
        return resp

    def get_info_from_public_api(self, name, info):
        country_info = self.country_info.get_info(name)
        if country_info is None:
            return self.public_api_error
        if 'all' in info:
            return country_info
        response = {}
        for i in info:
            if i not in country_info:
                return self.invalid_info
            response[i] = country_info[i]
        return response