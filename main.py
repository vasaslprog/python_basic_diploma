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


