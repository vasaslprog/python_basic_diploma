import datetime
from api.find_matches_by_day import find_matches_by_date
from api.find_cur_league import sorted_info_by_league
from telebot.types import Message
from loader import bot
from database.models import History


@bot.message_handler(commands=["today_matches"])
def handler_today_matches(message: Message) -> None:
    date_of_event = str(datetime.date.today()).replace('-', '')

    find_matches_by_date(your_date=date_of_event)
    matches_list = sorted_info_by_league()

    if len(matches_list) > 0:
        bot.reply_to(message, "Список матчей сегодня:\n" + "\n".join(map(str, matches_list)))
    else:
        bot.reply_to(message, "\nНет матчей сегодня."
                              r"Попробуйте выбрать другую дату, используя команду /custom_matches")
    History.create(
        user=message.from_user.id,
        name_users=message.from_user.first_name,
        time_req=datetime.datetime.now(),
        command="today_matches",
        res_func=matches_list,
    )
