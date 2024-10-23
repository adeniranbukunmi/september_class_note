import mysql.connector as sql
from decouple import config

my_con = sql.connect(host=config('host'), user=config('user'), passwd=config('passwd'), db="registrationDb")

myCursor = my_con.cursor()
# myCursor.execute("CREATE DATABASE registrationDb")
# myCursor.close()
# print('done')
# myCursor.execute("SHOW DATABASES ")
# for db in myCursor.fetchall():
#     print(db)
# myCursor.close()


# myCursor.execute("SHOW DATABASES ")
# for num, db in enumerate(myCursor):
#     print(num,'>>>',db)
# myCursor.close()


# myCursor.execute("CREATE TABLE register(id INT(3) PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20), age INT(2), gender VARCHAR(6))")
# myCursor.close()
# print('done')


# myCursor.execute("SHOW COLUMNS FROM register ")
# for num, col in enumerate(myCursor):
#     print(num,'>>>',col)
# myCursor.close()


# myCursor.execute("ALTER TABLE register CHANGE reg_id user_regid INT(3) AUTO_INCREMENT")
# print('column renamed successfully')

# myCursor.execute("ALTER TABLE register ADD contact VARCHAR(11) UNIQUE")
# myCursor.close()
# print('column added successfully')

# myCursor.execute("ALTER TABLE register CHANGE email emails VARCHAR(50)")
# myCursor.close()
# print('column change successfully')

# my_query="INSERT INTO register (name, age, gender, emails,contact) VALUES(%s,%s,%s,%s,%s)"
# user_info=('tolu',24, 'female', 'tolu@gmail.com', "09012345678")
# myCursor.execute(my_query, user_info)
# my_con.commit()
# myCursor.close()
# print(f"{myCursor.rowcount} record inserted successfully")

# name = input("enter your name: ")
# age = input("enter your age: ")
# gender = input("type F for female or M for male: ")
# emails = input("enter your email: ")
# contact = input("enter your phone number: ")

# x=0
# for each in range(0, 9):
#     name = input("enter your name: ")
#     age = input("enter your age: ")
#     gender = input("type F for female or M for male: ")
#     emails = input("enter your email: ")
#     contact = input("enter your phone number: ")
#     # each_student=[input("enter first name: "),input("enter last name: "),input("enter username: "), input(" enter email: ")]
#     # students.append(each_student)
#     my_query="INSERT INTO register (name,age,gender,emails, contact) VALUES(%s,%s,%s,%s,%s)"
#     val=(name, age, gender, emails, contact)

#     try:
#         myCursor.execute(my_query, val)
#         x+=1
#         my_con.commit()
#     except sql.Error as e:
#         print(f"Error: {e}")
# print(f'{x} row successfully inserted')

# my_query="INSERT INTO register (name, age, gender, emails,contact) VALUES(%s,%s,%s,%s,%s)"
# user_info=(name,age, gender, emails, contact)
# myCursor.execute(my_query, user_info)
# my_con.commit()
# myCursor.close()
# print(f"{myCursor.rowcount} record inserted successfully")

# my_query= "SELECT * FROM register"
# myCursor.execute(my_query)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# query ="SELECT name, contact FROM register" 
# myCursor.execute(query)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# my_query="SELECT * FROM register WHERE emails=%s"
# user_info=('tj@gmail.com',)
# myCursor.execute(my_query, user_info)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# query ="SELECT name, contact FROM register WHERE age=%s"
# val=(24,) 
# myCursor.execute(query, val)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# to get the age range of student betw age 15
# query ="SELECT name, contact, age FROM register WHERE age>=15"
# # val=(24,) 
# myCursor.execute(query)
# for each in myCursor.fetchall():
#     print(each)
# myCursor.close()

# TO UPDATE A DATA ON A TABLE IN THE DATA BASE
# query= "UPDATE register SET emails='excel@gmail.com' WHERE emails=%s"
# val=("excel@g",)    
# myCursor.execute(query, val)
# my_con.commit()
# print(myCursor.rowcount, "record update successfully")

# name so you wont go and change all the username that users have input inside the database. 
# query= "UPDATE register SET age='17', name='Tikristinimi' WHERE emails=%s"
# val=("tk@gmail.com",)
# myCursor.execute(query, val)
# my_con.commit()
# print(myCursor.rowcount, "record update successfully")

# user = input("enter your name >>> ")
# email=input('enter your  email >>> ')
# query="SELECT name, emails FROM register WHERE name=%s AND emails=%s"
# val=(user, email)
# myCursor.execute(query, val)
# user_info= myCursor.fetchone()
# if user_info: #can also be written as 'if myreg True:'
#     print("access granted")
# else:
#     print("access denied kindly register")

# HOW TO DELETE FROM THE DATA BASE
# query= "DELETE FROM register  WHERE age=%s"
# val=(24,)
# myCursor.execute(query,val)
# my_con.commit()
# print(myCursor.rowcount, "record deleted successfully")

# HOW TO DELETE A TABLE FROM THE DATA BASE
# query= "DROP DATABASE  registrationDb"
# myCursor.execute(query) # deleted