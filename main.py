import requests
from twilio.rest import Client
import os

URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.getenv("OpenWeatherAPI")

account_sid = 'AC1eccdbe53e16f3d57848a451fca1da54'
auth_token = os.getenv("MY TWILIO AUTH TOKEN")

parameters = {
    "lat": 3.595196,
    "lon": 98.672226,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

with requests.get(URL, params=parameters) as connection:
    connection.raise_for_status()
    weather_data = connection.json()
    will_rain = False
    for _ in range(0, 11):
        condition_code = int(weather_data["hourly"][_]['weather'][0]["id"])
        if condition_code < 700:
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+15017122661',
            to='+15558675310'
        )

        print(message.sid)
