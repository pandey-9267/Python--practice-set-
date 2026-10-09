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