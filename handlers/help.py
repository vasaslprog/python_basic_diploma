from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message) -> None:
    text = [f"/{command} - {description}" for command, description in DEFAULT_COMMANDS]
    bot.reply_to(message, f"\nВы можете использовать следующие команды:\n{'\n'.join(text)}")
