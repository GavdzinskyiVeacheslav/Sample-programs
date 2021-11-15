import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('2fb7b73a709c0fb8d670c52d9f3e199b', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("1992611247:AAFKqBQmzkoQThkVaITEGxnRGDdWGx_9f3M")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "In the town " + message.text + " now " + w.detailed_status + "\n"
    answer += "Temperature in the area " + str(temp) + "\n\n"

    if temp < 10:
        answer += "It's very cold now, dress like a tank!"
    elif temp < 20:
        answer += "It's cold now, dress warmly!"
    else:
        answer += "Normal temperature, wear whatever"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

# @pogodaaa000pybot
