# basics of sets

# how to crete set 

collection = {1, 2, "abhishek"}
print(collection)

# how to create empty set 

# # this is wrong way this is the way for dict 

# null_set = {}
# print(type(null_set))

# correct way 

null_set = set()
print(type(null_set))

# length of the set 

print(len(collection))

# set did not give duplicate values into the output if it present in the set 

duplicate_set = {1, 2, 2, 5, 5, "money", "money"}
print(duplicate_set)
print(len(duplicate_set))