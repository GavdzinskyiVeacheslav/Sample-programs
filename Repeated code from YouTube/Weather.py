from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('2fb7b73a709c0fb8d670c52d9f3e199b', config_dict)
mgr = owm.weather_manager()

place = input("В каком Городе/Стране?:  ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас в районе " + str(temp))

if temp < 10:
    print("Сейчас очень холодно, одевайся как танк!")
elif temp < 20:
    print("Сейчас холодно, оденься потеплее.")
else:
    print("Температура норм, одевай что угодно")

