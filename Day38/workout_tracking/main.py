import requests
from datetime import datetime

APP_ID = "e0dcf480"
APP_KEY = "7da99f259c370061a8d8b528b649498d"

USERNAME = "giba"
PASSWORD = "E2bjxbkF"

headers = {
    "x-app-id": APP_ID,
    "x-app-key":APP_KEY,
}

workout_input = input("Enter workout detail: ")

body_params = {
    "query": workout_input,
    "gender": "male",
    "weight_kg": "83",
    "height_cm": "180.34",
    "age": "20",
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=body_params, headers=headers)
workout_data = response.json()

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
curr_time = today.strftime("%H:%M:%S")

for exercise in workout_data["exercises"]:
    sheet_inputs = {
        "workout": {
            'date': today_date,
            'time': curr_time,
            'exercise': exercise['name'].title(), 
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    TOKEN = "Bearer E2bjxbkF"
    headers = {
        "Authorization": TOKEN, 
    }

    response = requests.post(url="https://api.sheety.co/ae8f2aa5978b00e2f440d1592fe391bc/workoutTracker/workouts", json=sheet_inputs, headers=headers)
    print(response.text)




# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint, 
#   json=sheet_inputs, 
#   auth=(
#       YOUR USERNAME, 
#       YOUR PASSWORD,
#   )
# )

# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint, 
#     json=sheet_inputs, 
#     headers=bearer_headers
# )