import math

import requests
import json

URL = "https://currate.ru/api/"
TOKEN = "d27d0ccb04818709950aabfd72ba138b"
response = requests.get(URL + "?get=currency_list&key=" + TOKEN)
decoded_response = json.loads(response.text)
print(decoded_response)


