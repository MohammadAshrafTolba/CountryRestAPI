from flask import Flask
from flask_restful import Api
from offline_response_handler import OfflineResponseHandler

app = Flask(__name__)
api = Api(app)

api.add_resource(OfflineResponseHandler, '/country/name/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)