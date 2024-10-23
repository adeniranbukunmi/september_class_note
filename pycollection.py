"""
list
tuple
set
dictionary


Creating a list in Python
Creating a list with multiple distinct or duplicate elements
Getting the size of Python list
Accessing elements from the List
Negative indexing
Taking Input of a Python List
Adding Elements to a Python List
Using append() method
Using insert() method
Using extend() method
Reversing a List in Python
A list can be reversed by using the reverse() method in Python.
Using the reversed() function:
Removing Elements from the List
Using remove() method
Using pop() method
Slicing of a List
Negative index List slicing
List Comprehension
Basic Example on Python List
List Methods
Built-in functions with List
"""
list_of_item =['1', 3j, 6.8, True, ['Temi','Taiwo']]
list_of_studt2= list(['kiki',"bolu","tope", ["fole","grace","jola"]])
list_of_studt3= list(['kiki',"bolu","tope", ["fola","grace","jola"],'ayo',"bayo","fola" ])
list_of_studt4= [['kiki',"bolu","tope"], ["fola","grace"]]

# print(type(list_of_studt2))
# print(type(list_of_item))
# print(type(list_of_studt3))
# print(len(list_of_studt3))
# print(list_of_studt3[3][2])

# print(list_of_studt4[-2][1], list_of_studt4[1][1] )
# print(list_of_studt4[1][1])
# print(list_of_studt3[-3:-1])
# print(list_of_studt3[::-1])  #reversing
# list_of_studt3.reverse()
# print('reversing all the names: ', list_of_studt3)  #reversing

list_of_studt4.append('Temi')
list_of_studt4.append('Tikristi')
# print('appending a name: ', list_of_studt4)  #reversing

# class work
# collect 5 student name and age, store them in a variable and display the content of the variable in your terminal 

list_of_studt=[]

# for each in range(0, 3):
#     name=input("enter your name: ")
#     age=input("enter your age: ")
#     age_name= name, age
#     list_of_studt.append(age_name)
# print(list_of_studt)

# for each in range(0, 3):
#     age_name=[input("enter your name: "), input("enter your age: ")]
#     list_of_studt.append(age_name)
# print(list_of_studt)


# list_of_studt5= [['Aliu',"Habeeb","Fathima"], ["Sodiq","toheeb"]]
# list_of_studt4.extend(list_of_studt5)
# # print(list_of_studt4)
# list_of_studt4.insert(2, 'Habeebu')

# list_of_studt4.remove('Temi')
# # list_of_studt4.pop(1)
# list_of_studt4.pop()
# print(list_of_studt4)



# For list of strings/chars

# lst1 = []
# lst1 = [int(item) for item in input("Enter the list items: ").split()]
# print(lst1)


# name='tolu titi'
# print(name.split())

# itm=tuple('toluwalogo')
# # print(itm[1:4])
# print(itm[1:])  #to remove the first letter

"""
Creating a Tuple
Creating a Tuple with Mixed Datatypes.
Accessing of Python Tuples; they contain a sequence of heterogeneous elements that are accessed via unpacking or indexing
Concatenation of Tuples (must e the same datatype)
Slicing of Tuple
Deleting a Tuple
unpacking
"""

fruits=('mango','pawpaw')
fruits2=tuple(('mango','pawpaw', 'orange', 'apple'))
fruits3=('mango','pawpaw', 'mango','pawpaw', 3j, ("tami","dara", "taiwo", "tk",), ['cumcumber', 'banana'], {1 ,2,3})

# print(type(fruits2))
# print(len(fruits2))
# print(len(fruits3))
# print(fruits2[::-1])
# print(len(fruits3))
# print("findings:", fruits3[::2])
# print('\nindex 5: ',fruits3[5][0],'\n')

# for name in fruits3[7]:
#     print(name)


# unpacking
employee=(('Taiwo','taiwo123@gmail.com', 'liegeman', 'Male'), ('Dara','daradudu@gmail.com', 'doughnutBoy', 'Male'), ('Temi','iyagbogbo@gmail.com', 'iyagbogbo', 'Female'))

employee2=(('Taiwo','taiwo123@gmail.com', 'liegeman', 'Male'), ('Dara','daradudu@gmail.com', 'doughnutBoy', 'Male'), ('Temi','iyagbogbo@gmail.com', 'iyagbogbo', 'Female'), ('Tope','iyagbogbo2@gmail.com', '3iyagbogbo', 'Female'))
# emply1, emply2, emply3 =employee
# print(emply1[0], emply2[0], emply3[0]) 
emply1, *others, emply13 =employee2
# print(emply1)
# print(others)
# print(emply13)

# for _, email, _, _ in employee:
#     # print("name of all employees",name,"\n")
#     print("email of all employees",email,"\n")
    # print("username of all employees",username,"\n")
    # print("gender of all employees",gender,"\n")

# x=0
# for _, email, _, gender in employee:
#     x+=1
#     print(f"email and gender of  employee {x}  >>> {email} >>> {gender}\n")


#concatenation
# fruits5 = fruits + fruits2
# print(fruits5)
# print(fruits)
# del fruits
# print(fruits)


# SET
# Python Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.

# Creating a Set in Python
# Adding Elements to a Set in Python
# Using add() Method
# Using update() Method set1 = set([4, 5, (6, 7)])
# set1.update([10, 11])
# print(set1)

# Removing Elements from the Set in Python

# set1={1, 6, 3, 8, 7, 7,4,3}
# set2=set((8, 4, 3))

# print(type(set1))
# print(type(set2))
# set1.add(8)
# set1.update((12, 14, 15))
# set1.remove(15)
# set3=set1.copy()
# set1.add(10)
# print(set3)
# set1.union(set2)
# set3=set1.intersection(set2)
# set3=set1.difference(set2)
# set3=set2.issubset(set1)
# print(set3)
# # 3 set1 set2 set3


# list_of_sets =[]
# num_of_set=int(input('how many set do want to work with>> '))
# for each_set in range(1, num_of_set+1):
#     set_items=[]
#     items=int(input(f'how many values are in set {each_set}>> '))
#     for itm in range(1, items+1):
#         item=input(f'enter value {itm}>> ')
#         set_items.append(item)
#     list_of_sets.append(set(set_items))
# print(list_of_sets)

# dictionary
"""
how to create a dictionary
how to access 
adding item
deleting
nested dict
"""

electronics={'Laptop':'Lenovo', "phone":"samsung", "mifi":'Mtn',"cug":'Mtn'}
electronics2= dict([(12, 'hp'), (13, 'del')])
electronics3=dict(fruit1='mango', fruit2='orange')
# print(type(electronics3))
# print(type(electronics))
# print(type(electronics2[1]))
# print(electronics2[1])
# print(len(electronics2))
# print(len(electronics))
# print(len(electronics2))
# print(electronics2.keys())
# print(electronics2.values())
# print(electronics['Lenovo'])

# electronics.update(dict(year=2021, color="white"))
# electronics.update(dict(year=2024, color="blue"))
# electronics.update(dict(Laptop='Mac book Pro'))
# # electronics.pop("phone")
# # electronics.popitem()
# del electronics['mifi']
# print(electronics)
# # classes_of_food.pop('class1')
# # print(classes_of_food)
# # classes_of_food.popitem()
# print(classes_of_food)
# del product['model']
# print(product)
# classes_of_food.clear()


# for keys, value in electronics.items():
#     print(keys)

questions={ '1.what is the capital of nigeria a)ogbomoso b)abuja':"b",
            '':"",
            '':"",
            '':"",

    }

# create a cbt question application
# solution

questions = {
    "1.What is 2 + 2?\n (a)22 (b)4 (c)8 :\n ": "b",
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

# for each in range(0,5):
#     name= input("enter your name: ")
#     matric_number= input("enter your matric number: ")
#     registered_students[matric_number]= name
    
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
#     print(f"\n{matric_number}, your score is {score}/100.\n")
        
#     if each < 4:
#         next_student = input("Is the next student available to take the CBT test? (yes/no): ").lower()
#         if next_student != 'yes':
#             print("Test terminated.")
#             break
        
# print(""" 1. login 2. register """)

# registered_student = []

# for name in range(1, 6):
#     registered_name = input('Name: ')
#     registered_matricno = int(input('Matric no: '))     
#     student = registered_name, registered_matricno
#     registered_student.append(student)
# print(registered_student)

# for items in range(1, 6):
#     name = input('\nWhat is your name? ')
#     matric_no = int(input('What is your matric no? '))
#     student_details = name, matric_no
#     if student_details in registered_student:
#         ask_student = input('\nAre you ready to take this test (Yes or No)? ')
#         if ask_student == "Yes":
#             score = 0
#             cbt_questions = {
#                 '1. Who is the current President of Nigeria? a) Muhammadu Buhari b) Bola Ahmed Tinubu c) Yemi Osibanjo d) Goodluck Johnathan': 'b',
#                 '2. In what year did Nigeria gain independence from Britain? a) 1960 b) 1963 c) 1957 d) 1970' : 'a',
#                 '3. Which Nigerian state recently became the largest oil producer? a) Akwa Ibom b) Delta c) Rivers d) Lagos' : 'a',
#                 '4. Who is the current Governor of the Central Bank of Nigeria (CBN)? a) Godwin Emefiele b) Folashodun Shonubi c) Lamido Sanusi d) Zainab Ahmed' : 'b',
#                 '5. Which Nigerian University was recently ranked highest in Africa in Times Higher Education Marketing? a) University of Lagos b)University of Ibadan c) Covenant University d) Obafemi Awolowo University' : 'c',
#                 '6. The Nigerian national minimum wage was recently raised to what amount? a) #30,000 b) #50,000 c) #100,000 d) #70,000' : 'd',
#                 '7. Which Nigerian artist won the Grammy Award for Best Global Music Album in 2021? a) Burna Boy b) Wizkid c) Davido d) Tiwa Savage' :'a',
#                 '8. The Lekki Toll Gate shooting during the #ENDSARS protests happened in which year? a) 2018 b) 2020 c) 2021 c) 2021 d) 2019' : 'b',
#                 '9. What is the capital of Nigeria? a) Lagos b) Port Harcourt c) Abuja d) Kano' : 'c',
#                 '10. Which Nigerian footballer recently signed a major deal with a European football club? a) Wilfred Ndidi b) Victor Oshimen c)Kelechi Iheanacho d) Samuel Chukwueze' : 'b',
#                 '11. The 2023 Nigerian Presidential election was held on what date? a) Februrary 25, 2023 b) March 10, 2023 c) April 1, 2023 d)January 31, 2023' : 'a',
#                 '12. Who is the current Minister of Foreign Affairs in Nigeria? a) Geoffrey Onyeama b) Zainab Ahmed c) Nyesom Wike d) Festus Keyamo' :'a',
#                 '13. The Nigerian national football team is also known as what? a) The Black Stars b) The Desert Warriors c)The Indomitable Lions d)The Super Eagles' : 'd',
#                 '14. Which state is the largest by population in Nigeria? a) Lagos b) Kano c) Kaduna d) Rivers' : 'a',
#                 '15. Who is the current Chief Justice of Nigeria (CJN)? a) Ibrahim Tanko Muhammad b) Walter Onnoghen c) Olukayode Ariwoola d) Mahmud Mohammed' : 'c'
#                 }
#             for question, answer in cbt_questions.items():
#                 print(question)
#                 ans = input('Answer: ')
#                 if ans == answer:
#                     score+=1
#                     percentage = round((score/15)*100)
#             print(f'Dear, {name} you have {percentage}%'.center(100))
#         else:
#             print('Cancel')
#     else:
#         print('You were not registered for this course')
#     if items < 4:
#         ask_user = input('Is the next person available for the test (Yes or No)? ')
#         if ask_user != 'Yes':
#             print('Test Terminated')



