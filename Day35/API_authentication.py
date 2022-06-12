import requests

api_key = "8a2a7ca3a88261efe4effac8d34d7d7c"

MY_LATITUDE = 20.297470
MY_LONGITUDE = 85.825220

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
    if ((500 <= int(condition_code) < 600) and (will_rain == False)):
        will_rain = True

if will_rain:
    print("Bring an umbrella")



