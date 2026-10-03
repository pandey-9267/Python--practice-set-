# Basics of the file input_output

# f = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "r")
# file = f.read()
# print(file)
# print(type(file))
# f.close()

# How to read file (by character)

# f = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "r")
# data = f.read(8)
# print(data)
# f.close()

# and if want to read line by line then

# file = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "r")
# line_1 = file.readline()
# print(line_1)
# file.close

# line_2 = file.readline()
# print(line_2)
# file.close()

# How to write in a file

# overwrite_in_file = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "w")
# overwrite_in_file.write("Leraning how to overwrite in the existing file")  # overwrites the entrie file
# overwrite_in_file.close()

# How to add a line in the existing file without overwrites

# add_in_file = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "a")
# add_in_file.write("\nLearing how to append in a file")
# add_in_file.close()

# Another syntax for these opertion 

# this only write the data from the file 

# with open ("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# by this the exsiting data of the file completely remove and show only which is written below 

# with open("D:\AIML(practice set)\Python(practice set)\input_output\demo.txt", "w") as f:
#     f.write("This is the another way of writing in the file")     

# for removing a file or deleting the file we have to use import 

# import os
# os.remove("D:\AIML(practice set)\Python(practice set)\input_output\sample.txt")

# -------------------------------------------------------------------------------------------

# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

# with open("D:\AIML(practice set)\Python(practice set)\input_output\practice.txt", "w") as f:
#     f.write("Hi everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java")

# -------------------------------------------

# WAF that replaces all occurrences of “java” with “python” in above file.

# with open(r"D:\AIML(practice set)\Python(practice set)\input_output\practice.txt", "r") as f:
#     data = f.read()
# edited_file = data.replace("Java", "Python")
# print(edited_file)

# with open(r"D:\AIML(practice set)\Python(practice set)\input_output\practice.txt", "w") as f:
#     f.write(edited_file)

# -------------------------------------------

# Search if the word “learning” exists in the file or not.

# def check_word():
#     word = "learning"
#     with open(
#         r"D:\AIML(practice set)\Python(practice set)\input_output\practice.txt","r") as f:
#         data = f.read()
#     if word in data:
#         print("Found")
#     else:
#         print("Not found")

# check_word()

# ---------------------------------------------------

# WAF to find in which line of the file does the word “learning” occur first. Print -1 if word not found.

# def check_for_line():
#     word = "1111"
#     data = True
#     line_no = 1
#     with open(r"D:\AIML(practice set)\Python(practice set)\input_output\practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 return
#             line_no += 1

#     return -1

# print(check_for_line())

# HOW THIS IS WORKING
# +----------------------+
# | Start                |
# +----------+-----------+
#            |
#            v
# +----------------------+
# | word = "1111"       |
# | data = True         |
# | line_no = 1         |
# +----------+-----------+
#            |
#            v
# +----------------------+
# | Open practice.txt   |
# +----------+-----------+
#            |
#            v
# +----------------------+
# | while data is True? |
# +----+------------+----+
#      | Yes        | No
#      v            v
# +----------------+  +----------------------+
# | Read one line  |  | return -1            |
# | using readline |  | word was not found  |
# +-------+--------+  +----------------------+
#         |
#         v
# +----------------------+
# | Is "1111" in line?  |
# +----+------------+----+
#      | Yes        | No
#      v            v
# +----------------+  +----------------------+
# | return None    |  | line_no = line_no+1 |
# | due to return  |  +----------+-----------+
# +----------------+             |
#                                |
#                                +------+
#                                       |
#                                       v
#                          +----------------------+
#                          | Read next line       |
#                          +----------------------+

