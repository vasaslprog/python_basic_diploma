import datetime
import re

from api.find_matches_by_day import find_matches_by_date
from api.find_cur_league import sorted_info_by_league
from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["custom_matches"])
def handler_today_matches(message: Message):
    bot.reply_to(message, "Укажите дату в формате гггг-мм-дд, например 2025-02-25")
    bot.register_next_step_handler(message, check_and_run)


def check_and_run(msg):
    date_text = msg.text
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if date_pattern.match(date_text):
        print("сходится!")

        date_of_event = str(date_text).replace("-", "")

        find_matches_by_date(your_date=date_of_event)
        matches_list = sorted_info_by_league()
        bot.reply_to(msg, '\n'.join(map(str, matches_list)))
