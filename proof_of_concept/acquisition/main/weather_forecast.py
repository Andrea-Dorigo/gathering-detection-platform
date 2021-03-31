
# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
from datetime import datetime
import pymongo

# MongoDB parameters
CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DATABASE = CLIENT["GDP-test"]
COLLECTION = DATABASE["weather_forecast"]

# OpenWeather API key
API_KEY = "550617cb3af649e1d6729a3f78b24e17"

# Base OpenWeatherMap api url
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"

def get_hourly_forecast(latitude,longitude):

    # url to request
    complete_url = ( BASE_URL +
                    "lat=" + str(latitude) +
                    "&lon=" + str(longitude) + "&exclude=current,minutely,daily,alert" +
                    "&units=metric" +
                    "&appid=" + API_KEY )

    # Api request to get weather data, save it into a json
    response = requests.get(complete_url).json()
    # print(response)

    for i in range(48):
        # get the complete forecast for hour i
        y = response["hourly"][i]

        # get temperature, forecast hour, weather_description
        forecast_hour = datetime.fromtimestamp(y["dt"])
        weather_description = y["weather"][0]["description"]
        temperature = y["temp"]

        # print values for that hour
        print(" temperature = " + str(temperature) +
              "\n forecast_hour = " + str(forecast_hour) +
              "\n description = " + str(weather_description))

        COLLECTION.insert_one({ "latitude" : latitude ,
                                "longitude" : longitude ,
                                "datetime" : forecast_hour,
                                "weather_description" : weather_description,
                                "temperature" : temperature })



get_hourly_forecast(41.899139,12.473311)
