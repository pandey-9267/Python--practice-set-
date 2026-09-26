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

overwrite_in_file = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "w")
overwrite_in_file.write("Leraning how to overwrite in the existing file")  # overwrites the entrie file
overwrite_in_file.close()

# How to add a line in the existing file without overwrites

add_in_file = open("D:\\AIML(practice set)\\Python(practice set)\\input_output\\demo.txt", "a")
add_in_file.write("\nLearing how to append in a file")
add_in_file.close()