import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DB_PATH = r"..\database.db"
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("today_matches", "Вывести матчи на сегодня"),
    ("custom_matches", "Вывести матчи на указанную дату"),
    ("history", "Вывести последние ваши 10 запросов"),
)
