from flask import Flask
from flask_restful import Api
from API.response_handler import ResponseHandler
from API.country_info import CountryInfo
import requests


app = Flask(__name__)
api = Api(app)

#   Just routing to the ResponseHandler class
@app.route("/country/name/<string:name>/keys/<string:keys>")
def route_scenario_1(name, keys):
    handler = ResponseHandler()
    response = handler.get(name, keys)
    return response

@app.route("/country/name/<string:name>/keys/")
@app.route("/country/name/<string:name>/")
def route_scenario_2(name):
    handler = ResponseHandler()
    response = handler.get_all_info(name)
    return response

if __name__ == '__main__':
    app.run(debug=True)