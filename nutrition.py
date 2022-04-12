import json

import requests

APIKEY = "/6yRpFLwTHvriZaYu9X08g==iR3nMv3bujN7DkUT"
APIURL = "https://api.api-ninjas.com/v1/nutrition?query="
class NutritionAPI():

    def getNutritionData(self, query):
        api_url = APIURL + query
        response = self.__getResponse(api_url)[0]
        message = self.__iterateDictionary(response)
        message = message.replace("_", " ")
        return response

    def __iterateDictionary(self, dictionary):
        message = ""
        for key in dictionary:
            message += key + ": " + str(dictionary[key]) + "\n"
        return message

    def __getResponse(self, api_url):
        response = requests.get(api_url, headers={'X-Api-Key': APIKEY})
        response = json.loads(response.content.decode('UTF-8'))
        return response
