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
