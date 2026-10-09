# What is abstration 
# Abstraction focuses on what an object does, rather than how it does it.

# Example

# class Car_abstr:

#     def __init__ (self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start (self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...")

# car1 = Car_abstr()
# car1.start()

# Whati is Encapculation
# Encapsulation protects data by controlling how it is accessed and modified.

# -----------------------------------------

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

# class Account:

#     def __init__ (self, acc_no, bal):
#         self.account_no = acc_no
#         self.balance = bal

#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"rs. {amount} is debited from your account")
#         self.total_amount()

#     # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print(f"rs. {amount} is credited in your account")
#         self.total_amount()

#     # printing the total left balance method
#     def total_amount(self):
#         print(f"Total balance in you account is : {self.balance}")

# acc1 = Account(236547, 10000)
# # print(f"Your account no. is : {acc1.account_no}")
# # print(f"Balance in you account : {acc1.balance}")

# acc1.debit(1000)
# acc1.credit(2500)
# acc1.credit(40000)
# acc1.debit(15000)

# What is Inheritance?

# Inheritance allows a child class to reuse and extend the functionality of a parent class.

# There are 3 types of inheritance
# 1. Single inheritance
# 2. Multi-line inheritance
# 3. Mutiple inheritance

# Example : single inheritance (Single inheritance means one child class inherits from one parent class.)

# class Car:

#     color = "Black"

#     @staticmethod
#     def start ():
#         print("Car started...")

#     @staticmethod
#     def stop ():
#         print("Car stoped")

# class ToyotaCar (Car):

#     def __init__(self,name):
#         self.name = name

# car1  = ToyotaCar("Fortuner")
# print(car1.color)
# car1.start()
# car1.stop()

# Example : Multi-line inheritance (In multilevel inheritance, a class inherits from another child class, forming a chain.)

# class Car:

#     @staticmethod
#     def start ():
#         print("Car started...")

#     @staticmethod
#     def stop ():
#         print("Car stoped")

# class ToyotaCar (Car):

#     def __init__(self,name):
#         self.name = name

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Disel")
# car1.start()
# car1.stop()

# Example : Multiple inheritance (In multiple inheritance, one child class inherits from two or more parent classes.)

# class A:
#     valA = "Welcome to Class A"


# class B:
#     valB = "Welcome to Class B"


# class C(A, B):
#     valC = "Welcome to Class C"

# c1 = C()
# print(c1.valC)
# print(c1.valB)
# print(c1.valA)

# What is polymorphism ?

# ``````````````````````````````

# -------------------------------------

# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:

#     def __init__(self, radius):
#         self.radius = radius 
    
#     def Area(self):
#         return 3.14 * self.radius ** 2

#     def Perimeter(self):
#         return 2 * 3.14 * self.radius

# cir1 = Circle(7)
# print(f"Area of the circle: {cir1.Area()}")
# print(f"Perimeter od the circle: {cir1.Perimeter()}")

# ----------------------------------------------

# Define an Employee class with attributes role, department & salary. This class has a showDetails( ) method.
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age

# class Employee:

#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")

# class Engineer(Employee):
#     def __init__(self, name, age):
#         super().__init__("Software Developer", "Testing", "45,000")
#         self.name = name
#         self.age = age

#     def showDetails(self):
#         print(f"Name: {self.name}")
#         print(f"Department: {self.age}")
#         super().showDetails()


# emp1 = Engineer("Abhishek", 20)
# emp1.showDetails()

# -------------------------------------------------

# WE also learn here how to implemet the dunder function

# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

# class Order:
#     def __init__ (self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price < odr2.price


# odr1 = Order("PS5", 1145)
# odr2 = Order("All games", 145)

# print(odr1 < odr2) # True
# print(odr1 > odr2) # False