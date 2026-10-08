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

class Students:

    def __init__ (self, name):
        self.name = name
        print("Add Students details here: ")

s1 = Students("Abhishek")
print(s1.name)

# this print dilip and the abhishek is still there bcoz The first box ("Abhishek") is now lost in memory because the s1 note was taken off it.
s1 = Students("Dilip")    
print(s1.name)

s2 = Students("Asraf")
print(s2.name)