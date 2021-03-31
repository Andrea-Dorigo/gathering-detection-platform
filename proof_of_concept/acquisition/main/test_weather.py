
# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json
from datetime import datetime


def get_future_weather(latitude,longitude):
    # Enter your API key here
    api_key = "550617cb3af649e1d6729a3f78b24e17"

    # base_url variable to store url
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"

    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

    # Give city name
    # city_name = "Rome"

    # lat = "41.899139"
    # lon = "12.473311"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "lat=" + str(latitude) + "&lon=" + str(longitude) + "&exclude=current,minutely,daily,alert" + "&units=metric" + "&appid=" + api_key


    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # print(response)
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    #print(x)

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal 550617cb3af649e1d6729a3f78b24e17
    # "404", means city is found otherwise,
    # city is not found

    # store the value of "main"
    # key in variable y

    y = x["hourly"][1]
    print(y)
    # store the value corresponding
    # to the "temp" key of y
    temperature = y["temp"]
    hour = datetime.fromtimestamp(y["dt"])
    # >>> datetime.fromtimestamp(1485714600).strftime("%A, %B %d, %Y %I:%M:%S")


    # store the value corresponding
    # to the "pressure" key of y
    # current_pressure = y["pressure"]
    #
    # # store the value corresponding
    # # to the "humidity" key of y
    # current_humidiy = y["humidity"]

    # store the value of "weather"
    # key in variable z
    #z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    #weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in Celsius unit) = " +
                    str(temperature) +
          # "\n atmospheric pressure (in hPa unit) = " +
          #           str(current_pressure) +
          # "\n humidity (in percentage) = " +
          #           str(current_humidiy) +
          "\n hour = " +
                    str(hour))
    #return [current_temperature, weather_description]

get_future_weather(41.899139,12.473311)
