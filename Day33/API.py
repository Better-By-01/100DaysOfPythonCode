# WHAT IS AN API ?

#     --> Application Programming Interface is a set of commands, functions, protocols, and objects 
#         that programmers can use to create software or interact with an external system.

#     --> API is a menu like we have in restaurents as an interface between the customer and the kitchen.

# API Endpoint ?        (a url)
#     --> Location where the data is stored 
#     --> like if we want to get the money out of the bank then we need to know where that bank is & what is it's address

# API request ?
#     --> Going to the bank and trying to get some money out we make a request to the teller for the money we want 
#         elese everything will become chaotic.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
response.raise_for_status()     # it raises exception if the HTTP request returned an unsuccessful status code

data = response.json()["iss_position"]["latitude"]
# print(data)

#OR
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)                # https://www.latlong.net/Show-Latitude-Longitude.html
print(iss_position)


# Response codes (for more https://www.webfx.com/web-development/glossary/http-status-codes/)
# 404 -> whatever we are looking for doesn't exist
# 1XX -> Hold On something is happening this is not final
# 2XX -> Here you Go
# 3XX -> Go away (no permission)
# 4XX -> We screwed up (and the thing we are looking for doesn't exist)
# 5XX -> I screwed up (I -> server)

