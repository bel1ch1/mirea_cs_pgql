# libraries
import psycopg2
import PyQt6
# Подключение к базе данных
connetction = psycopg2.connect(
    database="",
    user="",
    password="",
    host="127.0.0.1",
    port="5432"
)


curs = connetction.cursor()



# entry point
#if __name__ == "__main":
