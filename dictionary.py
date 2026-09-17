# dict = {
#     "name" : "abhi",
#     "cgpa" : 7.1,
#     "marks" : [80, 98, 78]
# }
# print(dict)

# # accessong the key in dict

# print(dict["name"])

# # for repalcing the value 

# dict["name"] = "Abhishek"
# print(dict)

# # also add a new key vlaue 

# dict["surname"] = "pandey"
# print(dict)

# # how to add key value in a empty or null dict

# null_dict = {}
# null_dict["name"] = "Anush"
# print(null_dict)

# How nested dictionay work

students = {
    "Name" : "Rahul",
    "Subjects" : {
        "chem" : 88,
        "Phy" : 98,
        "Pyhton" : 100
    }
}

print(students)
print(students["Subjects"])
print(students["Subjects"] ["Pyhton"])