import requests
import json

def getWeather():
    weatherURL = 'http://api.weatherapi.com/v1/current.json'
    dealershipCity = 'Richmond, VA'
    token = '8a39ae98fba84251a16230215211204'
    PARAMS = {
        'q' : dealershipCity,
        'key' : token
    }

    req = requests.get(url= weatherURL, params=PARAMS)

    res = req.json()
    print(res)

    weatherCondition = res['current']['condition']['text']
    weatherIcon = res['current']['condition']['icon']
    weatherTemp = f"{res['current']['temp_f']}\u00B0"

    weatherObj = {
        'condition': weatherCondition,
        'icon': weatherIcon,
        'temp': weatherTemp
    }
    return weatherObj


def requestTimeToAirport():
    """ Google Directions API request for 'Time to Airport' Data """
    airportURL = 'https://maps.googleapis.com/maps/api/directions/json?'
    dealershipAddress = '9520 W Broad St, Richmond, VA'
    airport = 'Richmond International Airport'

    PARAMS = {
        'origin' : dealershipAddress,
        'destination' : airport,
        'key' : 'API_KEY'
    }

    req = requests.get(url= airportURL, params= PARAMS)

    res = req.json()
    timeToAirport = res['routes'][0]['legs'][0]['duration']['text']
    return timeToAirport