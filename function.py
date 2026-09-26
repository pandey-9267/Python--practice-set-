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

# -----------------------------------------

# Write a recursion function to calculate the sum of first n natural numbers 

def calc_sum(n):
    if (n == 0):
        return 0
    return n + calc_sum(n-1)

print(calc_sum(5))

# Step-by-Step Breakdown for calc_sum(5)
# calc_sum(5) calls 5 + calc_sum(4)
# calc_sum(4) calls 4 + calc_sum(3)
# calc_sum(3) calls 3 + calc_sum(2)
# calc_sum(2) calls 2 + calc_sum(1)
# calc_sum(1) calls 1 + calc_sum(0)
# calc_sum(0) hits the base case and returns 0
# Now the values unwind and add up:
# calc_sum(1) returns 1 + 0 = 1
# calc_sum(2) returns 2 + 1 = 3
# calc_sum(3) returns 3 + 3 = 6
# calc_sum(4) returns 4 + 6 = 10
# calc_sum(5) returns 5 + 10 = 15

# ---------------------------------------------

# Write a recursive function to print all elements in a list.
# (Hint : use list & index as parameters)

# def print_list(list, idx = 0):
#     if (idx == len(list)):
#         return
#     print(list[idx], end = " ")   # end = " " is used for printing the output in the horizontally 
#     print_list(list, idx+1)

# fruites = ["Apple", "Mango", "Banana", "Pineapple"]
# print_list(fruites)

# how the above code is working step by step 

# fruites = ["Apple", "Mango", "Banana", "Pineapple"]

# print_list(fruites, 0)
#         |
#         v
# idx = 0, idx != len(fruites) [4]
# print(fruites[0])  -> Apple
# print_list(fruites, 1)
#         |
#         v
# idx = 1
# print(fruites[1])  -> Mango
# print_list(fruites, 2)
#         |
#         v
# idx = 2
# print(fruites[2])  -> Banana
# print_list(fruites, 3)
#         |
#         v
# idx = 3
# print(fruites[3])  -> Pineapple
# print_list(fruites, 4)
#         |
#         v
# idx == len(fruites) [4]
# return