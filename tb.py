import mysql.connector as sql
from decouple import config



my_con = sql.connect(host=config('host'), user=config('user'), passwd=config('passwd'))

my_cusor=my_con.cursor()