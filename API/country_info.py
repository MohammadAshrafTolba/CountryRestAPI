import requests

class CountryInfo:

    def get_info(self, country_name):

        # defining our core url
        url = 'https://restcountries.eu/rest/v2/name/{name}'

        # concatenating the given country name to the url
        url = url.format(name=country_name)

        try:
        # return the required info ftom the url
            response = requests.get(url).json()
        # checking fot requests exceptions
        except requests.RequestException:
            return None
        if len(response) == 0:
            return None
        return response[0]
