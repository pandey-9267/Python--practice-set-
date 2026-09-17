# # dict = {
# #     "name" : "abhi",
# #     "cgpa" : 7.1,
# #     "marks" : [80, 98, 78]
# # }
# # print(dict)

# # # accessong the key in dict

# # print(dict["name"])

# # # for repalcing the value 

# # dict["name"] = "Abhishek"
# # print(dict)

# # # also add a new key vlaue 

# # dict["surname"] = "pandey"
# # print(dict)

# # # how to add key value in a empty or null dict

# # null_dict = {}
# # null_dict["name"] = "Anush"
# # print(null_dict)

# # How nested dictionay work

# # students = {
# #     "Name" : "Rahul",
# #     "Subjects" : {
# #         "chem" : 88,
# #         "Phy" : 98,
# #         "Pyhton" : 100
# #     }
# # }

# # print(students)
# # print(students["Subjects"])
# # print(students["Subjects"] ["Pyhton"])

# # METHODS
# students = {
#       "Name" : "Rahul",
#       "Subjects" : {
#           "chem" : 88,
#           "Phy" : 98,
#           "Pyhton" : 100
#       }
#   }

# # this return all the keys 

# print(students.keys())

# # this convert in to list or anything you want do like this 

# print(list(students))
# print(tuple(students))

# # this return all the values 

# print(students.values())

# # this return the length of the dict 

# print(len(students))

# # this return all the key value pairs in the tuple

# # print(students.items())

# # and if want to access the single tuple from the above 

# pairs = list(students.items())
# print(pairs[0])

# # retuen the kay according to the value
# # there are two ways 

# # print(students["Name"])  

# # this way give an    error  this is not not bcoz after error other lines of code which is correct that also not run 
# # print(students["name2"]) 


# print(students.get("Name"))

# # # this way did not give erroe is give   none but here the runs the all line 
# print(students.get("name2"))

# # update the dict 

# # students.update({"city" : "Delhi"})
# # print(students)

# # also do like this 

# new_dict = {"city" : "Delhi"}
# students.update(new_dict)
# print(students)

# ---------------------------------------------

# Store following word meanings in a python dictionary
# table : "a piece of furniture", "list of facts & figures"cat : "a small animal"

things = {
    "table" : ["a piece of furniture", "list of facts & fiures"],
    "cat" : "a small animal"
}
print(things)