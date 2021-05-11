import requests, json

def get_current_weather(latitude,longitude):
    # compose API url
    api_key = "550617cb3af649e1d6729a3f78b24e17"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "lat=" + str(latitude) + "&lon=" + str(longitude) + "&units=metric" + "&appid=" + api_key

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] == 200:
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return [current_temperature, weather_description]

    else:
        print(" Request didn't return 200 ")

# get_current_weather(41.899139,12.473311)
