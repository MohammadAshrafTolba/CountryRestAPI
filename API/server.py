from flask import Flask
from flask_restful import Api
from response_handler import ResponseHandler
import requests

app = Flask(__name__)
api = Api(app)

# routing path to the DataHandler class
api.add_resource(ResponseHandler, '/country/name/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
