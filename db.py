import psycopg2

def connect_to_db():
    connection = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="5660126",
        database="journal_db"
    )

    connection.autocommit = True  # чтобы не делать коммиты каждый раз, делаем автокоммит
    return connection
# cursor = connection.cursor()


def get_cursor():
    return cursor
