# basics of sets

# # how to crete set 

# collection = {1, 2, "abhishek"}
# print(collection)

# how to create empty set 

# # this is wrong way this is the way for dict 

# null_set = {}
# print(type(null_set))

# # correct way 

# null_set = set()
# print(type(null_set))

# # length of the set 

# print(len(collection))

# # set did not give duplicate values into the output if it present in the set 

# duplicate_set = {1, 2, 2, 5, 5, "money", "money"}
# print(duplicate_set)
# print(len(duplicate_set))

# methods of the sets

# add a element in a set 

method = set()
method.add(1)
method.add(2)
method.add(2)
method.add("Abhishek")
method.add("Pandey")
method.add((1,2,3,4))
# this give error bocz the element of the set are immutable is cannot  add list and dict
# method.add([1, 2, "abhishek"])  
print(method)

# remove the element from the set 

method.remove(1)
print(method)
print(len(method))

# clear the whole set 

method.clear()
print(len("method"))

# remove a random value 

# this give a random value 

set_1 = {"Abhishek", "pandey", "B.tech", "CSE", "4th", "year", "7th", "Sem"}
print(set_1.pop())
print(set_1.pop())

# uninon of set 

age_1 = {25, 25, 23, 78, 95, 15}
age_2 = {23, 26, 24, 49, 15, 95}
print(age_1.union(age_2))

# intersection of set 

print(age_1.intersection(age_2))

# sort the set   here we use    sorted not not

print(sorted(age_1.union(age_2)))
print(sorted(age_1.intersection(age_2)))