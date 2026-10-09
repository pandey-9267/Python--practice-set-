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
#         print(f"Rs. {amount} is debited from your account")
#         self.total_amount()

#     # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} is credited in your account")
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