import requests
import ast


class CountryInfo:

    def get_info(self, country_name):

        # defining our core url
        url = 'https://restcountries.eu/rest/v2/name/{name}'

        # concatenating the given country name to the url
        url = url.format(name=country_name)

        try:

        # return the required info ftom the url
            response = requests.get(url)
            from_cache = False

            if response.status_code == 200:

                if response.from_cache:
                    print("[FROM CACHE]")
                    from_cache = True

                #byte_response = response.content
                #dict = byte_response.decode("UTF-8")
                response = response.json()[0]
                cache_status = {'from cache': from_cache}
                response.update(cache_status)
                return response

            else:
                return None
        # checking for requests exceptions
        except requests.RequestException:
            return None
