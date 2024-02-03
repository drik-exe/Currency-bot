from telebot import types
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Выбрать другой банк', 'Выбрать другую валюту', 'Курс на текущий день')

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчики для каждого действия
@bot.message_handler(func=lambda message: message.text == 'Выбрать другой банк')
def choose_bank(message):
    # Здесь можно добавить логику для выбора другого банка
    bot.send_message(message.chat.id, "Вы выбрали действие 'Выбрать другой банк'")

@bot.message_handler(func=lambda message: message.text == 'Выбрать другую валюту')
def choose_currency(message):
    # Здесь можно добавить логику для выбора другой валюты
    bot.send_message(message.chat.id, "Вы выбрали действие 'Выбрать другую валюту'")

@bot.message_handler(func=lambda message: message.text == 'Курс на текущий день')
def current_exchange_rate(message):
    # Здесь можно добавить логику для получения курса на текущий день
    bot.send_message(message.chat.id, "Вы выбрали действие 'Курс на текущий день'")

# Обработчик для действия "Курс на выбранный день"
@bot.message_handler(func=lambda message: message.text == 'Курс на выбранный день')
def custom_exchange_rate(message):
    # Здесь можно добавить логику для получения курса на выбранный день
    bot.send_message(message.chat.id, "Вы выбрали действие 'Курс на выбранный день'")


