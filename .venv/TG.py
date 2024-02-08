import telebot # pyTelegramBotAPI - название библиотеки
from telebot import types
import csv
from getphone import bot
from getphone import geophone
# bot = telebot.TeleBot('6614082297:AAHaw515vBXmQ9suDSi8IpHiyrgLz45R30Q')

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Авторизоваться")
    # btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup1.add(btn1)
    bot.send_message(message.chat.id, text="Здраствуйте, {0.first_name}! Я чат-бот Автомакс. Для продожения работы необходимо авторизоваться!".format(message.from_user), reply_markup=markup1)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Авторизоваться"):
        geophone(message);


if __name__ == '__main__':
     bot.infinity_polling()