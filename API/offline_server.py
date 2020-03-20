from flask import Flask
from flask_restful import Api
from API.offline_response_handler import OfflineResponseHandler

app = Flask(__name__)
api = Api(app)

api.add_resource(OfflineResponseHandler, '/country/name/<string:name>')
@app.route("/country/name/<string:name>/keys/<string:keys>")
def route_scenario_1(name, keys):
    handler = OfflineResponseHandler()
    response = handler.get(name, keys)
    return response

@app.route("/country/name/<string:name>/keys/")
@app.route("/country/name/<string:name>/")
def route_scenario_2(name):
    handler = OfflineResponseHandler()
    response = handler.get_all_info(name)
    return response


if __name__ == '__main__':
    app.run(debug=True)