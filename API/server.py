from flask import Flask
from flask_restful import Api
from data_handler import DataHandler

app = Flask(__name__)
api = Api(app)

# routing path to the DataHandler class
api.add_resource(DataHandler, '//country/name/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)