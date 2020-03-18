from response_handler import ResponseHandler

def get_egypt_info():
    with open('offline_country_info.txt', 'r') as file:
        egypt_info = file.read()

class OfflineCountryInfo:
    def get_info(self, name):
        if name.lower() != 'egypt':
            return None
        egypt_info = get_egypt_info()
        return egypt_info

class OfflineResponseHandler(ResponseHandler):
    def __init__(self):
        super().__init__()
        self.info_api = OfflineCountryInfo()