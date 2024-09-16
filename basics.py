
#single line commenting
#below is  multiline commenting
# print("""
# wonni won wa mi won ni\n won wa mi am in sanfrancisco jamming
# """)
# escape characters: \n(new line)

# print("i am now a certified python developer")


"""
variable definition
variable declaration
variable rules
naming conventions
"""
# student_name='Temi','Dara',"Tikristi","Taiwo"
# print(student_name)
# _name='bolu'
# print(type(_name))

# the name must be descriptive
# you should not start naming with numbering 
# do not use reserve words for naming
# no spacing in between names
# you cant use special characters to begin your naming

fruits='agbalumo','mango'
fruit2='agbalumo'
# &jdh='titi'

# pascal
# snake case
# camel casing

nameOfStudent='Grace'   #camel casing
name_of_student='Grace'   #snake casing
NameOfStudent='Grace'   #pascal casing


# inbuilt python function
# print(type(fruits))
# print(type(fruit2))
# print(len(fruit2))
# names_of_student=input('what is you name: ')
# class work: 

# name_of_patient=input("what is you name>>>> ")
# first_time_patient=input("""is this you first time here>>>>
#                             type: 'yes i am new' or 'no i am not a new patient'
#                                             >>>  """)
# age=input("how old are you>>>> ")
# address=input("where do you live>>>> ")
# concatenation + or , or F

# print('my name is '+name_of_patient+' i am '+age+ 'years old.\n'+' i live at '+address+' and '+first_time_patient)
# print('my name is',name_of_patient,' i am ',age, 'years old.\n',' i live at ',address,' and ',first_time_patient)
# print(f'my name is {name_of_patient} i am {age}years old.\n i live at {address} and {first_time_patient}')

# operators 
"""
what is operators
type of operator
precedence (PEMDAS)


"""
# operators
# python OPERATORS AND IT USES
# In Python programming, Operators in general are used to perform operations on values and variables.
# Types of Operators in Python
#1 Arithmetic Operators
#2 Comparison Operators
#3 Logical Operators
#4 Assignment Operators
#5 Identity Operators and Membership Operators
"""
Operators	
#1 Arithmetic Operators

+	Addition: adds two operands:	x + y
–	Subtraction: subtracts two operands	x – y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when the first operand is divided by the second	x % y
**	Power: Returns first raised to power second operand	x ** y
"""
# print(10%4)
"""
Comparison Operators in Python

>	Greater than: True if the left operand is greater than the right	x > y
<	Less than: True if the left operand is less than the right	x < y
==	Equal to: True if both operands are equal	x == y
!=	Not equal to – True if operands are not equal	x != y
>=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
<=	Less than or equal to True if the left operand is less than or equal to the right	x <= y
"""

"""
Logical Operators in Python
and	: True if both the operands are true	x and y
or: True if either of the operands is true 	x or y
not	: True if the operand is false 	not x

"""
# value1=[]
# res=bool(value1)
# print('boo',res)
# print('not: ', not res)
# value2=()
# print(not value2)

# a= 'mango'
# b='orange'
# if len(a) or len(b) == 5:
#     print("both has the same length")
# else:
#     print("na lie! both are not of the same length")

x = 24
y = 20
list_item = [10, 20, 30, 40, 50] 
# if (x not in list): 
# 	print("x is NOT present in given list") 
# else: 
# 	print("x is present in given list") 
    


# score=0
# question=input('what is your name: ')
# ans=['Tikristi', 'bukunmi']
# if question in ans:
#     score+=5
#     print('correct! you just score',score)
# else:
#     print('oh nooo! you scored', score)


# a = 10
# b = a 
# print(b) 
# b += a 
# print(b) 
# b -= a 
# print(b) 
# b *= a 
# print(b) 
# b <<= a 
# print(b)
# b>>=a
# print('result of b:', b)
    # a=11
    # b=3
    # b -=a
    # print(b)

"""
Assignment Operators in Python
a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)
"""
"""
Membership Operators in Python
x = 24
y = 20
list = [10, 20, 30, 40, 50] 

if (x not in list): 
	print("x is NOT present in given list") 
else: 
	print("x is present in given list") 

if (y in list): 
	print("y is present in given list") 
else: 
	print("y is NOT present in given list") 

"""

"""
Bitwise Operators in Python
Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<

eg

a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 

Bitwise operators are commonly used in low-level programming, cryptography, and optimization tasks where direct manipulation of binary representations is necessary.
"""
value1=11
value2=10
result=value1 +value2
result2=value1 ** value2
result3=value1 % value2
# print('addition of two operand is :', result)
# print('power of operand one is :', result2)
# print('modulus of operand one is :', result3)
# x=1
# val1=range(1, 3)
# val2=range(1, 4)
# ans=val1 * val2
# print(f"multiplication table {x}", ans)
# x+=1

# num=int(input("enter a number: "))
# result= num % 2
# if num == '':
#     print("cant be empty")
# elif result == 0:
#     print("the number you supplied is an even number")
# elif result == 1:
#     print("the number you supplied is an odd number")
# else:
#     print("invalid entry")

# num_input = input("Enter a number: ")
# num_input.lstrip
# if num_input == '':
    # print("Input can't be empty")  #the empty entry must be check before converting to int
# elif num_input.lstrip('-').isdigit():  # Check if the input is a valid integer (including negative numbers)
#     num = int(num_input)
#     result = num % 2
#     if result == 0:
#         print("The number you supplied is an even number")
#     elif result != 0:  # This elif is technically not needed, but included as requested
#         print("The number you supplied is an odd number")
# else:
#     print("Invalid entry. Please enter a valid integer.")

# val=5 < 5
# print(val)

# fruit1='mangos'
# fruit2='orange'
# if len(fruit1) and len(fruit2) == 6:
#     print('both fruit has equal length')
# elif len(fruit1) and len(fruit2) !=6:
#     print('no match')
# elif len(fruit1) or len(fruit2) == 6:
#     print('one of the  fruit has  length 5')
# else:
#     print('invalid entry')

# bonus=2
# score=6
# score +=bonus
# print('you now have a bonus of', score)

# for num in range(2, 10):
#     num *=bonus
#     print(num)
# print('done')

x = 24
# y = 20
# list = [10, 20, 30, 40, 50] 

# if (x not in list): 
# 	print("x is NOT present in given list") 
# else: 
# 	print("x is present in given list") 

# if (y in list): 
# 	print("y is present in given list") 
# else: 
# 	print("y is NOT present in given list") 

"""
what string
string declaration
string methods
indexing
slicing
format
data type conversion
"""	

name='          fukufmi olaranwaju'
# print(len(name))
# print(name.strip().capitalize())
# name[0]='B'
# print(name)
# print(name.replace('f', 'b', 1))
# indexing
            # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
            # D a r a s i m i a m a   l  a  d  u d  u
student_name='Darasimiamaladudu'
# strings, methods

# new_name=student_name[0:13] + 'lafun'
# new_name=[student_name]

# print(student_name[3:0])    #this wont print anything because you can only slice from lowest index to the highest
# new_name[13:]='pupa'
# print(new_name)
# print(type(new_name))

# 6
# print(type(each_num))

lst = []
n = input("Enter number of elements : ")
 
for i in range(0, int(n)):
    each_info= [input('fisrt  value: '), input('second value: '), input('name; ')]
    lst.append(each_info)
 
print(lst)
print(lst[1])


# For list of integers
lst1 = []
 
# For list of strings/chars
# lst2 = []
 
# lst1 = [int(item) for item in input("Enter \
#                 the list items : ").split()]
 
# lst2 = [item for item in input("Enter \
#                 the list items : ").split()]
 
# print(lst1)
# print(lst2)