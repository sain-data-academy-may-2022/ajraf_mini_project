from multiprocessing import connection
import pymysql
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_db = os.environ.get("mysql_db")

def establish_conection():
    connection = pymysql.connect(
    host = my_host,
    user = my_user,
    password = my_password,
    database = my_db
    )
    return connection

def close_connection_and_cursor(connection,cursor):
    connection.commit()
    cursor.close()
    connection.close()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

from datetime import datetime

def current_date_prefix():
    date = datetime.today().strftime('%Y-%m-%d')
    date = date[5:]
    date = date.replace('-','/').replace('0',"")
    date = (f'2022/{date}')
    return date
