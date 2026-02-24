import requests
import json
import pyttsx3
from config import api
engine = pyttsx3.init()
city=input("Enter the city: ")
url=f"https://api.weatherapi.com/v1/current.json?key={api}&q={city}"
r=requests.get(url)
# print(r.text)
dic=json.loads(r.text)
temp_and_condition=(f"Tempertature {dic["current"]["temp_c"]}, It\'s {dic["current"]["condition"]["text"]} in {city}")
print(temp_and_condition)
engine.say(temp_and_condition)
engine.runAndWait()