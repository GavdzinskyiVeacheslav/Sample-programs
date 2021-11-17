""" The program receives weather data from the server for the entered city and tells you how to dress """

from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('2fb7b73a709c0fb8d670c52d9f3e199b', config_dict)
mgr = owm.weather_manager()

place = input("Which City/Country?:  ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("In the town " + place + " now " + w.detailed_status)
print("The temperature is now in the area " + str(temp))

if temp < 10:
    print("It's very cold now, dress like a tank!")
elif temp < 20:
    print("It's cold now, dress warmly.")
else:
    print("Normal temperature, wear whatever")

