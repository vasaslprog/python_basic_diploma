from telebot.types import Message
from loader import bot
from peewee import IntegrityError
from database.models import User


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, f"{first_name}, добро пожаловать в мой чат-бот! Я бот, который поможет тебе "
                              f"найти информацию о матчах Английской Премьер-лиги.\n"
                              f"Хотите посмотреть информацию о матчах?")
    except IntegrityError:
        bot.reply_to(message, f"{first_name}, рад вас снова видеть! Хотите посмотреть информацию о матчах?")


@bot.message_handler(content_types="text")
def message_reply(message: Message):
    if message.text.lower() in ["привет", "здравствуйте"]:
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        try:
            User.create(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            bot.reply_to(message, f"{first_name}, добро пожаловать в мой чат-бот!")
        except IntegrityError:
            bot.reply_to(message, f"{first_name}, рад вас снова видеть!")
