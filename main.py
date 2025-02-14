import database.models
from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter


if __name__ == "__main__":
    database.models.create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()


# import telebot
# from dotenv import load_dotenv
# import os
# from telebot import types
# import datetime
# import re
# from own_api.own_api import find_matches_by_date
# from find_cur_league import sorted_info_by_league

# load_dotenv()
# bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
#
#
# @bot.message_handler(commands=["start"])
# def main(message):
#     file = open('./ENG_PR_LEAGUE.jpg', 'rb')
#     bot.send_photo(message.chat.id, file)
#     bot.send_message(message.chat.id,
#                      f"Привет {message.from_user.first_name}! Я бот, который поможет тебе "
#                      f"найти информацию о матчах Английской Премьер-лиги."
#                      f"\nЖелаете узнать информацию о матче?")
#     markup = types.InlineKeyboardMarkup()
#     btn_yes = types.InlineKeyboardButton('Да', callback_data='да')
#     btn_no = types.InlineKeyboardButton('Нет', callback_data='нет')
#     markup.row(btn_yes, btn_no)
    # if message.text.lower() == 'да':
    #     bot.register_next_step_handler(message, choose_date)
    # else:
    #     bot.reply_to(message, "Бот завершил свою работу. Для возобновления нажмите старт")


# def choose_date(message):
#     if message.text.lower() == 'да':
#         markup = types.InlineKeyboardMarkup()
#         btn1 = types.InlineKeyboardButton('Сегодня', callback_data='today')
#         btn2 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
#         btn3 = types.InlineKeyboardButton('Послезавтра', callback_data='the day after tomorrow')
#         btn4 = types.InlineKeyboardButton('Напишите свою дату', callback_data='your date')
#         markup.row(btn1, btn2, btn3)
#         markup.add(btn4)
#         bot.send_message(message.chat.id, "Выберите дату матчей:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Бот завершил свою работу. Для возобновления нажмите старт")
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     date_of_event = None
#     if call.data == 'today':
#         date_of_event = str(datetime.date.today()).replace('-', '')
#     elif call.data == 'tomorrow':
#         date_of_event = (str(datetime.date.today() + datetime.timedelta(days=1))).replace('-', '')
#     elif call.data == 'the day after tomorrow':
#         date_of_event = (str(datetime.date.today() + datetime.timedelta(days=2))).replace('-', '')
#     elif call.data == 'your date':
#         bot.send_message(call.message.chat.id, "Напишите дату, используя формат ГГГГ-ММ-ДД")
#         bot.register_next_step_handler(call.message, choose_your_date)
#     if date_of_event:
#         find_matches_by_date(your_date=date_of_event)
#         matches_list = sorted_info_by_league()
#         print("Это 1!", matches_list)
#         bot.send_message(call.message.chat.id, '\n'.join(map(str, matches_list)))
#
#
# def choose_your_date(msg):
#     date_text = msg.text
#     date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
#     if date_pattern.match(date_text):
#         print("сходится!")
#         #  дописать ф-ю на проверку даты
#         date_of_event = str(date_text).replace("-", "")
#         find_matches_by_date(your_date=date_of_event)
#         matches_list = sorted_info_by_league()
#         print("Это 2!", matches_list)
#         bot.send_message(msg.chat.id, '\n'.join(map(str, matches_list)))
#
#     else:
#         print("не сходится!")


