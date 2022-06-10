from inspect import Parameter
import requests
from datetime import datetime

parameters = {
    "lat" : 20.296059,
    "lng" : 85.824539,
    "formatted" : 0,            # to get 24 hr format to match datetime.now() and not AM/PM
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise_hr = data["results"]["sunrise"]
sunrise_hr = sunrise_hr.split("T")[1].split(":")[0]
print(sunrise_hr)

sunset_hr = data["results"]["sunset"]
sunset_hr = sunset_hr.split("T")[1].split(":")[0]
print(sunset_hr)

curr_date = datetime.now()
print(curr_date.hour)