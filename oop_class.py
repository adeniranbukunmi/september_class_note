"""
OOP
how to create a class
what is class
what object
attribute
initializing
instance
inheritance
methods
"""

# # class Animal:
# #     def sleep(self):
# #         # self.name = name
# #         print(self.name, 'is the dog is sleeping')
# #         # return self.name

# # bullDog=Animal()
# # localDog=Animal()
# # germanShepard=Animal()
# # print(bullDog.sleep('bulldog'))

# class Employee:
#     """
#     3 paremeter name: location and salary
#     """
#     bonus=0.3 
#     def __init__(self, name, location, salary):
#         self.name = name
#         self.location = location
#         self.salary = salary
        
#     def  staff_detail(self):
#         detail=(f'my name is {self.name} and i am from {self.location}. my salary is {self.salary}')
#         # print(detail)
#         return detail
    
#     def anual_bonus(self):
    
#         self.salary=self.salary * self.bonus
#         return self.salary
    

# emp1=Employee('shalom', 'lagos', 10000)
# emp2=Employee('joshua', 'niger', 5000)
# emp3=Employee('tesleem', 'oyo', 2000)

# # emp1.name='shalom'
# # emp1.location='lagos'
# # emp1.salary=10000

# # emp2.name='joshua'
# # emp2.location='niger'
# # emp2.salary=5000

# # emp3.name='Tesleem'
# # emp3.location='Oyo'
# # emp3.salary=2000

# print("for emp1 details: ", emp1.staff_detail())
# print()
# print("for emp2 detail: ",emp2.staff_detail())
# print("for emp1 bonus: ",emp1.anual_bonus())
# print("for emp2 bonus: ",emp2.anual_bonus())   
# print("for emp3 bonus: ",emp3.anual_bonus())



# class StoreSale:
#     pass

# StoreSale1=StoreSale()
# StoreSale1.name="milo"
# StoreSale1.price=2600
# StoreSale1.date='2024/08/4'


# StoreSale2=StoreSale()
# StoreSale2.name="milo"
# StoreSale2.price=2600
# StoreSale2.date='2024/08/4'

class StoreSale:
    bonus =0.3
    
    def __init__(self, name, price, date, quantity, sale_rep):
        self.name = name
        self.price = price
        self.date = date
        self.quantity = quantity
        self.sale_rep = sale_rep
        # self.total_cost = 0


    def  sale_report(self):
        self.total_cost= int(self.price)*int(self.quantity[0])
        print(self.total_cost, 'updated total cost ')
        report= (f"the product sold is {self.name} by {self.sale_rep}. the total price is {self.total_cost}")
        return report
    

    def give_bonus(self):
        print(self.total_cost, 'give bonu one')
        # self.total_cost= int(self.price)*int(self.quantity[0])
        
        give_b=self.total_cost * self.bonus
        print(give_b, 'bonus to remove')
        actual_b=self.total_cost - give_b
        
        return f"you have  a bonus of {self.bonus} and the money you are paying is {actual_b}"
        
    

StoreSale1=StoreSale('milo', "1800", '2024/08/4', "2 role", 'Temi')
StoreSale2=StoreSale('milk', "1400", '2024/08/4', "2 role", 'Taiwo')

# print(StoreSale1.name)
# print(StoreSale1.price)
# print( StoreSale2.name)
# print( StoreSale2.price)
# print( StoreSale2.bonus)
# print( StoreSale1.bonus)
print( StoreSale2.sale_report())
print( StoreSale2.give_bonus())


