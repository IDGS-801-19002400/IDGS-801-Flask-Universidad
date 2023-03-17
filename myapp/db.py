from decouple import config 
import pymysql

def connection():
    conn = pymysql.connect(host=config('MYSQL_HOST'),
                           user=config('MYSQL_USER'),
                           password=config('MYSQL_PASSWORD'),
                           db=config('MYSQL_DB'))
    return conn