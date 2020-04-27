import requests
import json

class CountryInfo:

    def get_info(self, country_name):

        # defining our core url
        url = 'https://restcountries.eu/rest/v2/name/{name}'

        # concatenating the given country name to the url
        url = url.format(name=country_name)

        try:
        # return the required info ftom the url
            response = requests.get(url)
            if response.status_code == 200:
                if response.from_cache:
                    print("Caching...")
                return json.loads(response.content)[0]
            else:
                return None
        # checking for requests exceptions
        except requests.RequestException:
            return None
