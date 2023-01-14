import requests
from datetime import datetime

import config

USERNAME = "jeli"
TOKEN = config.TOKEN

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graphID = "graph1"


graph_config = {
    "id": graphID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graphID}"

today = datetime.now()
print(today)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

print(today.strftime("%Y%m%d"))
put_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

put_config = {
    "quantity": "10"
}

# response = requests.put(url=put_endpoint, json=put_config, headers=headers)


# print(put_endpoint)
response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)