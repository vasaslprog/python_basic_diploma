import datetime
import re

from api.find_matches_by_day import find_matches_by_date
from api.find_cur_league import sorted_info_by_league
from telebot.types import Message
from loader import bot
from database.models import History


@bot.message_handler(commands=["custom_matches"])
def handler_today_matches(message: Message) -> None:
    bot.reply_to(message, "Укажите дату в формате гггг-мм-дд, например 2025-02-25")
    bot.register_next_step_handler(message, check_and_run)


def check_and_run(msg: Message) -> None:
    date_text = msg.text
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if date_pattern.match(date_text):
        date_of_event = str(date_text).replace("-", "")

        find_matches_by_date(your_date=date_of_event)
        matches_list = sorted_info_by_league()
        if len(matches_list) > 0:
            bot.reply_to(msg, f"Список матчей на дату {date_text}:\n" + "\n".join(map(str, matches_list)))
        else:
            bot.reply_to(msg, "\nНет матчей в выбранную вами дату."
                              r"Попробуйте выбрать другую дату, используя команду /custom_matches")
        History.create(
            user=msg.from_user.id,
            name_users=msg.from_user.first_name,
            time_req=datetime.datetime.now(),
            command="custom_matches",
            res_func=matches_list,
        )
