import telebot
from telebot import types
import datetime

bot = telebot.TeleBot("7653689159:AAFTfZVYJ2Icdt--vm30zXbSLMViLQNBW9E")
date_of_event = None


@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Сегодня', callback_data='today')
    btn2 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
    btn3 = types.InlineKeyboardButton('Послезавтра', callback_data='the day after tomorrow')
    btn4 = types.InlineKeyboardButton('Напишите свою дату', callback_data='your date')
    markup.row(btn1, btn2, btn3)
    markup.add(btn4)
    file = open('./ENG_PR_LEAGUE.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.reply_to(message, f"Привет {message.from_user.first_name}! Я бот, который поможет тебе найти "
                          "информацию о матчах Английской Премьер-лиги. Выберите дату матча:", reply_markup=markup)


@bot.message_handler(commands=["help"])
def main(message):
    bot.reply_to(message, "Для начала нужно выбрать дату или ввести ее в формате дд-мм-гггг. Например: 28-04-1989")


@bot.message_handler()
def greetings(message):
    if message.text.lower() in ['привет', 'hi', 'здорова', 'здравствуйте']:
        bot.reply_to(message, f"Привет {message.from_user.first_name}! Я бот, который поможет тебе найти "
                              "информацию о матчах Английской Премьер-лиги. Выберите дату матча:")


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global date_of_event
    if callback.data == 'today':
        date_of_event = str(datetime.date.today()).replace('-', '')
        print(date_of_event)
    elif callback.data == 'tomorrow':
        date_of_event = (str(datetime.date.today() + datetime.timedelta(days=1))).replace('-', '')
        print(date_of_event)
    elif callback.data == 'the day after tomorrow':
        date_of_event = (str(datetime.date.today() + datetime.timedelta(days=2))).replace('-', '')
        print(date_of_event)
    else:
        print(date_of_event)
if __name__ == "__main__":
    bot.infinity_polling()
