import requests
from datetime import datetime
import os

from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('EXERCISE_APP_ID')
API_KEY = os.getenv('EXERCISE_API_KEY')
SHEET_KEY = os.getenv('EXERCISE_SHEET_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

exercise_endpoint ="https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"https://api.sheety.co/{SHEET_KEY}/myWorkoutTracker/workouts"

GENDER = "female"
AGE = 22
WEIGHT_KG = 50.0
HEIGHT_CM = 155.0

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

workout = input("Tell me about your workout today :")
data ={

 "query": workout,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age": AGE

}
bearer_headers = {
"Authorization": f"Bearer {BEARER_TOKEN}"
}


response = requests.post(url=exercise_endpoint, headers=headers, json=data)
print(response.json())
result = response.json()
print(result)
now = datetime.now()
date = str(now.strftime("%d/%m/%y"))
time = str(now.strftime("%H:%M:%S"))

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],

        }
    }

sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)