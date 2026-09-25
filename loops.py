# basics of while loop

# count = 1
# while count <= 5:
#     print("Hello")
#     count += 1
# print(count)

# i = 1
# while i <= 5:
#     print("Abhishek", i)
#     i += 1

# # print 1 to 5 

# no = 1 
# while no <= 5:
#     print(no)
#     no += 1
# print("loop ended")

# # print form 5 to 1 

# num = 5
# while num >= 1:
#     print(num)
#     num -= 1
# print("loop ended")

# -----------------------------

# Print numbers from 1 to 100

# nums = 1
# while nums <= 100:
#     print(nums)
#     nums += 1
    
# -----------------------------

# Print numbers from 100 to 1

# numb = 100
# while numb >= 1:
#     print(numb)
#     numb -= 1

# ------------------------------------

# Print the multiplication table of a number n

# table = int(input("Enter your no. : "))
# multiple = 1
# while multi <= 10:
#     print(table*multiple)
#     multi += 1

# --------------------------------------------

# Print the elements of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# sq = 1
# while sq <= 10:
#     print(sq*sq)
#     sq += 1

# ---------------------------------------------

# Search for a number x in this tuple using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("Founded", i)
        break
    else: 
      print("Finding...")
    i += 1