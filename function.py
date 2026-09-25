# Basics of function

# def calc_sum(a, b):
#     return a + b

# print(calc_sum(1, 2))


# def print_hello():
#     print("Hello")

# print_hello()
# print_hello()

# def calc_avg(x, y, z):
#     sum = x + y + z
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(1, 2, 3)

# how default parameter work

# def cal_multi(a, b=5):
#     return a * b

# print(cal_multi(1))

# ----------------------------------------

# WAP to print the length of the list (list is the parameter)

# movies = ["Ironman", "Aminal", "PK", "Dangal"]
# fav_actor = ["Salman", "SRK", "AK", "Aamir", "Sanjay"]

# def print_len(list):
#     print(len(list))

# print_len(movies)
# print_len(fav_actor)

# ------------------------------------------------

# WAP to print the elements of a list in a single line (lis is the parameter)

# fav_actor = ["Salman", "SRK", "AK", "Aamir", "Sanjay"]

# def print_list(list):
#     for i in list:
#         print(i, end = " ")

# print_list(fav_actor)

# ----------------------------------------------------

# WAP to find the factorial of n (n is the parameter)

# n = int(input("Enter your number : "))
# def calc_fact(n):
#     fact = 1 
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
#     # return fact
        
# calc_fact(n)

# -------------------------------------------

# WAP to convert USD to INR

# def converter(usd_val):
#     inr_val = usd_val * 95.75
#     print(f"{usd_val} USD = {inr_val} INR")

# converter(5)
# converter(7)

# -----------------------------------------------

# Create a function where it can check thar the number entered by thr user is EVEN or ODD

# num = int(input("Enter your num. : "))
# def check_even_or_odd(n):
#     if n%2 == 0:
#         print("Entered no. is : EVEN")
#     else:
#         print("Entered no. is : ODD")
#     # return num
    
# check_even_or_odd(num)

# -------------------------------------------------------

# basics of recursion

# print n to 1  backward

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# return n! 

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(6))