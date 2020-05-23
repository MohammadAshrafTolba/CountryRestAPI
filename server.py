from flask import Flask
from flask_restful import Api
from response_handler import ResponseHandler
import requests_cache

app = Flask(__name__)
api = Api(app)

requests_cache.install_cache(cache_name='cache', backend='sqlite', expire_after=30)

#   Just routing to the ResponseHandler class

@app.route('/')
def index():
    return '<h1>Welcome</h1>'

@app.route("/country/name/<string:name>/keys/")
@app.route("/country/name/<string:name>/")
def route_scenario_1(name):
    handler = ResponseHandler()
    response = handler.get_all_info(name)
    return response

@app.route("/country/name/<string:name>/keys/<string:keys>")
def route_scenario_2(name, keys):
    handler = ResponseHandler()
    response = handler.get(name, keys)
    return response


if __name__ == '__main__':
    app.run(debug=True)