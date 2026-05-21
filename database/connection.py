import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    return conn
