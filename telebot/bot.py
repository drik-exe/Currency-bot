from config import TOKEN
from config import APIData
import requests
from telebot import types
import telebot
import datetime

bot = telebot.TeleBot(TOKEN)

api_data = APIData()


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Национальный банк", "Альфа банк", "Беларусьбанк")

    bot.send_message(
        message.chat.id,
        "Привет, чтобы воспользоваться функционалом "
        "бота сперва выберите банк из меню снизу.",
        reply_markup=markup,
    )


@bot.message_handler(
    func=lambda message: message.text
    in ("Национальный банк", "Альфа банк", "Беларусьбанк")
)
def choose_bank(message):
    api_data.bank = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('USD', 'EUR', 'GBP', 'JPY')
    bot.send_message(message.chat.id, f"Ты выбрал {message.text}."
                                      " Теперь выбери нужную тебе валюту ниже.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ('USD', 'EUR', 'GBP', 'JPY', 'Национальный банк', 'Альфа банк', 'Беларусьбанк'))
def choose_currency(message):
    if len(message.text) <= 4:
        api_data.currency = message.text
    else:
        api_data.bank = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if api_data.bank == 'Альфа банк':
        markup.add('Курс на текущий день', 'Выбрать другой банк', 'Выбрать другую валюту')
    else:
        markup.add(
            'Курс на текущий день',
            'Курс на выбранный день',
            'Собрать статистику',
            'Выбрать другой банк',
            'Выбрать другую валюту')

    bot.send_message(message.chat.id, f"Выбранная валюта: {api_data.currency}."
                                      f"  Выбранный банк: {api_data.bank}.", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == 'Курс на текущий день')
def choose_currency_for_now(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if api_data.bank == 'Альфа банк':
        markup.add('Курс на текущий день', 'Выбрать другой банк', 'Выбрать другую валюту')
    else:
        markup.add(
            'Курс на текущий день',
            'Курс на выбранный день',
            'Собрать статистику',
            'Выбрать другой банк',
            'Выбрать другую валюту')

    if api_data.bank == "Национальный банк":
        data = requests.get(f'http://127.0.0.1:8000/national_bank/{api_data.currency}/{str(datetime.datetime.now())[:10]}')
        bot.send_message(message.chat.id, f"{api_data.bank} - {api_data.currency} на {str(datetime.datetime.now())[:10]}")
        bot.send_message(message.chat.id, f"Курс: {data.json()}", reply_markup=markup)
        print(data.json())
    elif api_data.bank == 'Беларусьбанк':
        data = requests.get(
            f'http://127.0.0.1:8000/belarus_bank/{api_data.currency}/{str(datetime.datetime.now())[:10]}')
        bot.send_message(message.chat.id,
                         f"{api_data.bank} - {api_data.currency} на {str(datetime.datetime.now())[:10]}")
        print(data.json())
        bot.send_message(message.chat.id, f"Курс продажи: {data.json()}")
        bot.send_message(message.chat.id, f"Курс покупки: {data.json()}", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == 'Выбрать другой банк')
def choose_another_bank(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Национальный банк', 'Альфа банк', 'Беларусьбанк')
    bot.send_message(message.chat.id, f"Выберите банк из меню снизу.", reply_markup=markup)
    bot.register_next_step_handler(message, choose_currency)


@bot.message_handler(func=lambda message: message.text == 'Выбрать другую валюту')
def choose_another_currency(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('USD', 'EUR', 'GBP', 'JPY')
    bot.send_message(message.chat.id, f"Выберите нужную валюту снизу.", reply_markup=markup)
    bot.register_next_step_handler(message, choose_currency)


