import datetime
from own_api.find_matches_by_day import find_matches_by_date
from own_api.find_cur_league import sorted_info_by_league
from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["today_matches"])
def handler_today_matches(message: Message):
    date_of_event = str(datetime.date.today()).replace('-', '')
    find_matches_by_date(your_date=date_of_event)
    matches_list = sorted_info_by_league()

    bot.reply_to(message, '\n'.join(map(str, matches_list)))
