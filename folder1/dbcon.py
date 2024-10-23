
import mysql.connector as sql
from decouple import config


def makecon():
    myCon=sql.connect(host="127.0.0.1", user='root', passwd="olasunkanmi60@")
    myCursor =myCon.cursor()
    name=input("enter database name>>> ")
    myCursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    myCon.database = name
    print(f"database {name} created successfully")


# makecon()