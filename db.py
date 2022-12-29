"""Модуль подключения, проверки и инициализации БД, также возврает курсор для остальных модулей"""
from loguru import logger
import psycopg2

from config import PASSWORD


logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")

try:
    connection = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password=PASSWORD,
        database="journal_db"
    )
except Exception as ex:
    logger.error(ex)

connection.autocommit = True  # чтобы не делать коммиты каждый раз, делаем автокоммит
cursor = connection.cursor()

def get_cursor():
    return cursor


@logger.catch
def _init_db():
    """Инициализирует БД"""
    with open("createdb.sql", "r") as f:
        sql = f.read()
        cursor.execute(sql)


def check_db_exist():
    """Проверяет инициализирована ли БД, если нет - инициализирует"""
    try:
        cursor.execute("select * from works;")
    except Exception:
        logger.info("Инициализирую таблицу works")
        _init_db()
    else:
        logger.debug("База уже создана")


check_db_exist()
