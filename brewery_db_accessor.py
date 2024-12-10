import psycopg2
import concealed_vars as cv


def connect_to_db(db_name):
    conn = psycopg2.connect(
        dbname=db_name,
        user=cv.DB_USER,
        password=cv.COMMON_PASS,
        host='localhost'
    )
