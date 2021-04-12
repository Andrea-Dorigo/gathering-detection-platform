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
import pymongo

# MongoDB parameters
# MongoEngine would be more appropriate here
CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT["GDP-test"]
COLLECTION = DATABASE["weather_forecast"]

# OpenWeather API key
API_KEY = "550617cb3af649e1d6729a3f78b24e17"

# Base OpenWeatherMap api url
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"

# Webcams json path
PATH_WEBCAM_JSON = "../webcams.json"


def call_openweather_api(latitude,longitude,API_KEY):

    # url to request
    complete_url = ( BASE_URL +
                    "lat=" + str(latitude) +
                    "&lon=" + str(longitude) + "&exclude=current,minutely,daily,alert" +
                    "&units=metric" +
                    "&appid=" + API_KEY )

    # Api request to get weather data, save it into a json
    response = requests.get(complete_url).json()
    # print(response)


def get_hourly_forecast(latitude,longitude):
    """
    Gets hourly forecast for any given coordinates
    for the next 48 hours.
    Forecast variables: temperature, weather_description
    """

    call_openweather_api(latitude,longitude,API_KEY)

    for i in range(48):
        # get the complete forecast for hour i
        hourly_forecast = response["hourly"][i]

        # get temperature, forecast hour, weather_description
        forecast_hour = datetime.fromtimestamp(hourly_forecast["dt"])
        weather_description = hourly_forecast["weather"][0]["description"]
        temperature = hourly_forecast["temp"]

        # print values for that hour
        print(" temperature = " + str(temperature) +
              "\n forecast_hour = " + str(forecast_hour) +
              "\n description = " + str(weather_description))

        COLLECTION.insert_one({ "latitude" : latitude ,
                                "longitude" : longitude ,
                                "datetime" : forecast_hour,
                                "weather_description" : weather_description,
                                "temperature" : temperature })


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

    # infinite loop
    #MODIFICATO! NON CHIAMA PIU' LA FUNZIONE OGNI 2 GIORNI, MA 1
    while True:

        tomorrow = datetime.today() + timedelta(days=1)
        midnight = datetime.combine(tomorrow, datetime.min.time())

        # loop all webcams
        for webcam in json_data["webcams"]:
            get_hourly_forecast(webcam["latitude"], webcam["longitude"])

        # sleep 30 minutes (1800 seconds)
        # time.sleep(1800)
        #
        # # repeat (could be a repeat twice loop)
        # for webcam in json_data["webcams"]:
        #     get_hourly_forecast(webcam["latitude"], webcam["longitude"])

        # sleep until the next midnight
        time.sleep((midnight - datetime.now()).total_seconds())


main()
# get_hourly_forecast(45.309812,18.410428)
