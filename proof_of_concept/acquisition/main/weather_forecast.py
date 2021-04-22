"""
Python program to get weather foreacast every 30 minutes
for all cities in webcams.
Uses OpenWeatherMap API:
more information at -> https://openweathermap.org/api

created by Andrea Dorigo
"""

# import required modules
import time
from datetime import datetime, timedelta
import json
import requests
from mongoengine import *

connect("GDP-test", host = "localhost", port = 27017)

class weather_forecast(Document):
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    datetime = DateTimeField(required=True)
    weather_description = StringField()
    temperature = FloatField()

API_KEY = "550617cb3af649e1d6729a3f78b24e17"
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"
PATH_WEBCAM_JSON = "../webcams.json"


def get_onecall_api_response(latitude,longitude,API_KEY):
    """
    Calls the OpenWeatherMap OneCall API to get
    weather forecast for the next 48 hours (current hour included)
    in a json format.
    More info here: https://openweathermap.org/api/one-call-api
    """
    # url to request
    complete_url = ( BASE_URL +
                    "lat=" + str(latitude) +
                    "&lon=" + str(longitude) + "&exclude=current,minutely,daily,alert" +
                    "&units=metric" +
                    "&appid=" + API_KEY )

    # Api request to get weather data, save it into a json
    return requests.get(complete_url).json()


def get_hourly_forecast(latitude,longitude):
    """
    Gets hourly forecast for any given coordinates
    for the next 48 hours.
    Forecast variables: temperature, weather_description
    """

    response = get_onecall_api_response(latitude,longitude,API_KEY)
    # print(response)

    for i in range(48):
        # get the complete forecast for hour i
        hourly_forecast = response["hourly"][i]

        # get temperature, forecast hour, weather_description
        forecast_hour = datetime.fromtimestamp(hourly_forecast["dt"])
        weather_description = hourly_forecast["weather"][0]["description"]
        temperature = hourly_forecast["temp"]

        print(" temperature = " + str(temperature) +
              "\n forecast_hour = " + str(forecast_hour) +
              "\n description = " + str(weather_description))

        weather_forecast(
            latitude = latitude,
            longitude = longitude,
            datetime = forecast_hour,
            weather_description = weather_description,
            temperature = temperature
            ).save()


def main():
    """
    Get forecast data every 30 minutes
    starting from the next midnight;

    get the weather data at minutes 00/30 of every hour,
    since that is required by the current Machine Learning model
    """

    # load json with webcams data
    with open(PATH_WEBCAM_JSON) as fopen:
        json_data = json.load(fopen)

    # wait until midnight
    tomorrow = datetime.today() + timedelta(days=1)
    midnight = datetime.combine(tomorrow, datetime.min.time())
    print( "waiting until: " + str(midnight) +
           ";\ntime remaining: " + str(midnight - datetime.now()) )

    time.sleep((midnight - datetime.now()).total_seconds())

    while True:

        tomorrow = datetime.today() + timedelta(days=1)
        midnight = datetime.combine(tomorrow, datetime.min.time())

        # loop all webcams
        for webcam in json_data["webcams"]:
            get_hourly_forecast(webcam["latitude"], webcam["longitude"])

        time.sleep((midnight - datetime.now()).total_seconds())


main()
