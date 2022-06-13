import requests
from datetime import date, datetime, timedelta

USERNAME="giba"
TOKEN="E2bjxbkF"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ONCE ACCOUNT CREATED NO NEED OF BELOW 2 LINES
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# GRAPH CREATED
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)                # url to view to graph : https://pixe.la/v1/users/giba/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_creation_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.5",
}
# print(pixel_creation_params["date"])                          # 20220613

# TODAY'S DATA ADDED
# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
# print(response.text)

yesterday = today - timedelta(days=1)

yesterday_pixel_creation_params = {
    "date": yesterday.strftime("%Y%m%d") ,
    "quantity": "15",
}
# print(yesterday_pixel_creation_params["date"])                          # 20220612

# response = requests.post(url=pixel_creation_endpoint, json=yesterday_pixel_creation_params, headers=headers)
# print(response.text)

pixel_put_endpoint = f"{pixel_creation_endpoint}/{pixel_creation_params['date']}"

new_pixel_param = {
    "quantity": "7",
}

# EX. OF HTTP PUT REQUEST CHANGING YESTERDAY'S DATA
# response = requests.put(url=pixel_put_endpoint, json=new_pixel_param, headers=headers)
# print(response.text)


# EX. OF HTTP DELETE REQUEST 
delete_endpoint = f"{pixel_creation_endpoint}/{pixel_creation_params['date']}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)