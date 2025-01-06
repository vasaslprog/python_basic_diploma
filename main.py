import telebot

bot = telebot.TeleBot("7653689159:AAFTfZVYJ2Icdt--vm30zXbSLMViLQNBW9E")


@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}! Я бот, который поможет тебе найти "
                          "информацию о матчах Английской Премьер-лиги. Выберите дату матча:")


@bot.message_handler(commands=["help"])
def main(message):
    bot.reply_to(message, "Для начала нужно выбрать дату или ввести ее в формате дд-мм-гггг. Например: 28-04-1989")


@bot.message_handler()
def greetings(message):
    if message.text.lower() in ['привет', 'hi', 'здорова', 'здравствуйте']:
        bot.reply_to(message, f"Привет {message.from_user.first_name}! Я бот, который поможет тебе найти "
                              "информацию о матчах Английской Премьер-лиги. Выберите дату матча:")


if __name__ == "__main__":
    bot.infinity_polling()
