# How to create class

# class first_class:
#     name = "Abhishek"

# How to create object 

# s1 = first_class()
# print(s1.name)

# How to create constructor

# class example:

#     def __init__ (self):
#         pass

# Example of OOPs using the above concepts

# class Students:

#     def __init__ (self, name):
#         self.name = name
#         print("Add Students details here: ")

# s1 = Students("Abhishek")
# print(s1.name)

# # this print dilip and the abhishek is still there bcoz The first box ("Abhishek") is now lost in memory because the s1 note was taken off it.
# s1 = Students("Dilip")    
# print(s1.name)

# s2 = Students("Asraf")
# print(s2.name)

# The implementation of method

# class Children:

#     def __init__ (self, name, study, section, age):
#         self.name = name
#         self.study = study
#         self.section = section
#         self.age = age

#     def stu_name(self):
#         print(f"My name is : {self.name}")

#     def stu_class(self):
#         print(f"I am in class : {self.study}")

#     def stu_section(self):
#         print(f"My section is : {self.section}")

#     def stu_age(self):
#         print(f"My age is : {self.age}")

# s1 = Children("Abhishek", "12th", "B", 20)
# s1.stu_name()
# s1.stu_class()
# s1.stu_section()
# s1.stu_age()

# --------------------------------------------

# Create a student class that take name and marks of three students as argument in Constructor then create a method to print the average

# class Students:

#     def __init__ (self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg_of_stu(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             average = sum/3
#         print(f"The average marks of {self.name} is: {average}")

# s1 = Students("Abhishek", [95, 95, 80])
# s1.avg_of_stu()

# How to delete the object property or object itself

# class Name:

#     def __init__ (self, name):
#         self.name = name

# s1 = Name("Abhishek")
# print(s1.name)   # here this print the name 
# del s1.name      # it did not print the name bcoz we delete the object property
# del s1          # and here we deleted the whole object 