from telebot import types
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

BANK = ''

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Национальный банк', 'Альфа банк', 'Беларусьбанк')

    bot.send_message(message.chat.id, "Привет, чтобы воспользоваться функционалом "
                                      "бота сперва выберите банк из меню снизу.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ('Национальный банк', 'Альфа банк', 'Беларусьбанк'))
def choose_bank(message):
    BANK = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('USD', 'EUR', 'GBP', 'JPY')
    bot.send_message(message.chat.id, f"Ты выбрал {message.text}."
                                      " Теперь выбери нужную тебе валюту ниже.:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Выбрать другую валюту')
def choose_currency(message):
    bot.send_message(message.chat.id, "Вы выбрали действие 'Выбрать другую валюту'")

@bot.message_handler(func=lambda message: message.text == 'Курс на текущий день')
def current_exchange_rate(message):
    bot.send_message(message.chat.id, "Вы выбрали действие 'Курс на текущий день'")

@bot.message_handler(func=lambda message: message.text == 'Курс на выбранный день')
def custom_exchange_rate(message):
    bot.send_message(message.chat.id, "Вы выбрали действие 'Курс на выбранный день'")