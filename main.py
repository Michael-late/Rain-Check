
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(r"twilio.env")

lat = os.getenv("latitude")
long = os.getenv("longitude")
api_key = os.getenv("api_key")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
number = os.getenv("number")

#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
parameters = {
    "lat" : lat,
    "lon" : long,
    "cnt" : 4,
    "appid" : api_key
}   

client = Client(account_sid, auth_token)

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_datas = response.json()

weather_code = []
rain = False
for x in range(len(weather_datas["list"])):
    code = weather_datas["list"][x]["weather"][0]["id"]
    weather_code.append(code)
    if code < 700:
        rain = True

if rain:
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Whatsapp Gang, It is raining today",
        to=str(number)
        )
        print(message.status)
        


