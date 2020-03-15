from flask_restful import Resource, Api, reqparse
from country_info import CountryInfo

class DataHandler(Resource):

    def __init__(self):

        # skeleton