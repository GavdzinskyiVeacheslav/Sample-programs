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

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас очень холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Холодно, одевайся потеплее!"
    else:
        answer += "Температура норм, одевай что угодно"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

# @pogodaaa000pybot