import requests
from twilio.rest import Client 
import os

api_key=os.environ.get("OWM_API_KEY")

MY_LATITUDE = 20.297470
MY_LONGITUDE = 85.825220

account_sid = "AC1ad7901045f9691b7ba6b97cae816fc6"
auth_token = "d81c65cbdf2d68934ae18ca8f8c20599"

weather_params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE, 
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall" 

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if (500 <= int(condition_code) < 600):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☂️",
                        from_="+17164588302",
                        to="+917735927805",
                    )
    print(message.sid)

# environment variable:
# allows us to separate out our keys|secret stuff and various other variables away from where our code base is located.
# Type the following in the terminal:
# export OWM_API_KEY=8a2a7ca3a88261efe4effac8d34d7d7c
# to use it in the codebase
# api_key = os.environ.get("OWM_API_KEY")