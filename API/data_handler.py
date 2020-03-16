from flask_restful import Resource
from flask import jsonify
from country_info import CountryInfo

class DataHandler(Resource):

    def __init__(self):
        self.info = CountryInfo()


    def get(self, name):
        returned_info = self.info.get_info(name)
        if len(returned_info) == 0:
            return 'Invalid resources'
        return jsonify(returned_info)