# def landing_page():
#     print("""
#                     1. login
#                     2. register
#                     3.make enquiry
#                     4.exit

#         """)
#     user=input("select option>>> ")
#     if user == '1':
#         print("welcome ")
#     elif user == '2':
#         print("welcome!!! you can now register ")   
#     elif user == '3':
#         print("what do you want to know!!! oloju rangandan ")  
#     elif user == '4':
#             exit()

# landing_page()


# list_student=[]

# for i in range(0, 3):
#     name=input('name; ')
#     list_student.append(name)
#     # print(list_student)
# while True:
#     remove_name=input("remove your name: ")
#     if remove_name in list_student:
#         print()
#         list_student.remove(remove_name)
#         print(list_student)
#     elif len(list_student) == 0:
#         break

"""
parametrize funx✅
non parametrize funx✅
global variable.✅
local varible✅
parameter ✅
arguments✅
"""
z=10
# def add_num(x, y):
#     global b
#     b=25
#     q=18
#     sum_all=x +  8 + y +z +q
#     print(sum_all)
# add_num(4, 2)

# def subtract_num(j, k):
#     sub_all= b -j -  8 - k -z
#     print(sub_all)
# subtract_num(15, 2)

"""
types of arguments
1. default args
2. keyword args
3.positional args
4. arbitrary args
"""
# 1. default args
# def add_num(x=5, y=3):
#     global b
#     b=25
#     q=18
#     sum_all=x +  8 + y +z +q
#     print(sum_all)
# add_num()

# # 2. keyword args

# def college(name, location):
#     print(name, location)

# college(name="SQL", location="Yoaco")
# college(location="Yoaco", name="SQL")


# 3.positional args
# def college_class(college, level):
#     print(f"me name is Bolu I study at {college} and My level is {level}")

# college_class("SQI", "Level2")
# college_class("Level2", "SQI")

# 4. arbitrary args
# def college_class(*args):
#     print(f"me name is Bolu I study at {args[0]} and My level is {args[1]} abut to go {args[2]}")

# college_class("SQI", "Level2", "home", "titi", "bolutife")

# kwargs
# def college_class(**kwargs):
#     print(kwargs.keys())
#     print(kwargs.values())
#     print(kwargs.items())

# college_class(name="SQI", level="Level2", address="home", name2="titi", name3="bolutife")


# def landing_page():
#     print("""
#                     1. login
#                     2. register
#                     3.make enquiry
#                     4.exit

#         """)
#     user=input("select option>>> ")
#     if user == '1':
#         print("welcome ")
#     elif user == '2':
#         print("welcome!!! you can now register ")   
#     elif user == '3':
#         print("what do you want to know!!! oloju rangandan ")  
#     elif user == '4':
#             exit()

# landing_page()
# import time
# import sys
# data_plan=['1. daily', "2. weekly", "3.monthly", "4. next","5. back"]
# user_input=input("enter ussd code: ")
# while user_input.strip() != "*312#":
#     print("invalid code try again ")
#     user_input=input("enter ussd code: ")
# else:
#     print("""
#         1. data plan
#         2. social plan
#         3. borrow credit/recharge
#         4. next
# """)
# user_input=input("enter option: \n")
# if user_input.strip() == "1":
#     print("buy data ".center(100))
#     time.sleep(2)
#     for data in data_plan:
#         print(data)
# elif user_input.strip() == "2":
#     pass
# elif user_input.strip() == "3":
#     pass
# elif user_input.strip() == "4":
#     pass
# elif user_input.strip() == "5":
#     pass
# else:
#     print("invalid input")

# function
# by convention, you start the naming of a funx should start with small letter

# def addition():
#     val1=4
#     val2=5
#     res=val1+val2
#     print(res)

# def subtraction():
#     val1=4
#     val2=5
#     res=val1-val2
#     print(res)
# def division():
#     val1=4
#     val2=5
#     res=val1/val2
#     print(res)
# def goBack():
#     user_input=input("enter 1 to go back: \n")
#     if user_input.strip()=="1":
#         startApp()
#     else:
#         print('invalid input')
# def startApp():
#     print("""
#         1. addition
#         2. subtraction
#         3. division
#         4. exit
#     """)
#     user_input=input("enter option: \n")
#     if user_input.strip() == "1":
#         addition()
#     elif user_input.strip() == "2":
#         subtraction()
#     elif user_input.strip() == "3":
#         division()
#     elif user_input.strip() == "4":
#         # exit()
#         sys.exit(1)
#     else:
#         print("invalid input")

# startApp()

# create a cbt question application
# solution
import random
questions = {
    "1.What is 2 + 2?\n (a)22 (b)4 (c)8 \nanswer: ": "b",
    "2.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\n": "c",
    "3.What is 10 / 2?\n (a)3 (b)5 (c)12:\n ": "b",
    "4.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\n ": "d",
    "5.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\n ": "c",
    "6.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\n ": "c",
    "7.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\n  ": "a",
    "8.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\n ": "b",
    "9.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "b",
    "10.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "a"
}

# registered_students={}
# student_completed=[]

# for each in range(0,5):
#     name= input("enter your name: ").lower()
#     matric_number= input("enter your matric number: ")
#     registered_students[matric_number]= name
# print(registered_students)
    
# for each in range(0,5):
#     matric_number = input("Enter your matric no to check if you are eligible for the test: ")

#     if matric_number not in registered_students:
#         print(f"{matric_number}, you are not eligible for the test. Please register first.\n")
#         continue
#     ready = input(f"{matric_number}, are you ready to take the CBT test? (yes/no): ").lower()
#     if ready !='yes':
#         print('Test terminated.')
#         continue
#     score=0
#     for question, correct_answer in questions.items():
#         answer = input(question + " ")
#         if answer == correct_answer:
#             score += 10
#     print(f"\n{matric_number}, your score is {score}/100.\n".center(200))
        
#     if each < 4:
#         next_student = input("Is the next student available to take the CBT test? (yes/no): ").lower()
#         if next_student != 'yes':
#             print("Test terminated.")



# import random as rd
# pd_length=6
# pd=('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPKRSTUVWXYZ!@#$%^&')
# random_pd=''.join(random.sample(pd, pd_length))
# print(random_pd)
# num= rd.randint(0000, 9999)
# uba_acc_num= "20" + str(num)
# print(uba_acc_num)

# emails=input('enter your email: ').strip()
# username=emails[:emails.index("@")]
# domain_name=emails[emails.index("@")+1:]
# print(username, domain_name)

# import random

# #range of the values of a dice
# min_val = 1
# max_val = 6

# #to loop the rolling through user input
# roll_again = "yes"

# #loop
# while roll_again == "yes" or roll_again == "y":
#     print("Rolling The Dices...")
#     print("The Values are :")
    
#     #generating and printing 1st random integer from 1 to 6
#     print(random.randint(1, 6))
    
#     #generating and printing 2nd random integer from 1 to 6
#     print(random.randint(min_val, max_val))
    
#     #asking user to roll the dice again. Any input other than yes or y will terminate the loop
#     roll_again = input("Roll the Dices Again?") 
    
    




# registered_students = {}  
# students_completed = []   

# for each in range(0,3):
#     name = input("Register your name: ")
#     matric_number = input("Register your matric number: ")
#     print("Registration successful!")
#     registered_students[name] = matric_number 
# print(registered_students)
# print("hello 1", students_completed)
# for student_name in registered_students.keys():
    
#     if student_name in students_completed:
#         print(f"{student_name}, you have already taken the test. You cannot participate again.")
#         continue  
#     next_student = input(f"Is {student_name} available to take the CBT test? \n(yes/no): ").strip().lower()
    
#     if next_student != 'yes':
#         print(f"{student_name} is not available.")
#         continue
#     matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
#     if matric_number != registered_students[student_name]:
#         print(f"{student_name}, your matric number is incorrect. You are not eligible for the test.")
#         continue
#     # if student_name in students_completed:
#     #     print(f"{student_name}, you have already taken the test. You cannot participate again.")
#     #     continue

#     students_completed.append(student_name)
#     print("hello appended", students_completed)

#     ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

#     if ready != 'yes':
#         print(f"{student_name}, test terminated. You are not taking the test.")
#         continue

#     score = 0
#     random_questions = random.sample(list(questions.items()), 3) 
    
#     for question, correct_answer in random_questions:
#         answer = input(question + " ") 
#         if answer.lower() == correct_answer.lower():  
#             score += 10 
#     print(f"\n{student_name}, your score is {score}/50.\n")



















# registered_students={}
# students_completed=[]
# def student_list():
#     for each in range(0,3):
#         name=('Register your name: ')
#         matric_number=('Register your matric number: ')
#         # registered_students[name]= matric_number
#         registered_student = name, matric_number
#         registered_students.append(registered_student)
#     print(registered_students)
# student_list()

