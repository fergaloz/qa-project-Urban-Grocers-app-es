import requests

import configuration
import data
from data import user_body

response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json= user_body,
                         headers=data.headers)
print(response.status_code)
print(response.json())

atk= response.json()["authToken"]
print(atk)

def new_client(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                          json=kit_body,
                          headers=data.headers)



print(response.request)
print(response.status_code)
response_new =new_client(data.kit_body)

print(response_new.json())


