import database.models
from loader import bot
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter
import handlers
import api


if __name__ == "__main__":
    database.models.create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()




