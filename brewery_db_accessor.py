import psycopg2


def connect_to_db(db_name):
    conn = psycopg2.connect(
        dbname=db_name,
        user="postgres",
        password="your_password",
        host="localhost"
    )
