from telebot import types
import telebot
from config import TOKEN

import calendar
bot = telebot.TeleBot(TOKEN)
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP



CHOOSEN_DATE = ''
@bot.message_handler(commands=['start'])
def start(m):
    # Функционал кадендаря при нажати кнопки старт. Дата сохраняется в переменную CHOOSEN_DATE
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)
@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)
    CHOOSEN_DATE = result
    print(CHOOSEN_DATE)

