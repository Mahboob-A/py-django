# python--flow/a-various-operators.py
# 231224, Monday, 11.30 AM

''' A.  Membership Operators: Checks availability of a value in a sequence like list, tuple, dictionary, set etc.'''

# membership operators checks if a value is present in a sequence or not
# It deals with the membership/availability of a value in a sequence
# in, not in

# in: True if value/variable is member of a sequence
# not in: True if value/variable is not member of a sequence
names = ["John", "Jane", "Jack", "Jill"]
name = 'John'

print(name in names) # True
print(name not in names) # False

name2 = 'Johny'
print(name2 in names) # False
print(name2 not in names) # True

# In case of dictionaries, it checks if the key is present in the dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York", 
}

print("name" in data) # True
print("age" in data) # True
print("country" not in data) # True 

a = [1, 2,3 ]
b = [1, 2, 3]
print("is a and b ==): ", a in b) # False as a is not a sublist of b

''' B.  Identity Operators: Compares the memory locations/IDs of two objects'''
# Identity operators are used to check if two values (or variables) are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.
# Identity operators compares the id's of the objects, not the values of the objects.
# is, is not

a = 100 

b = 100 


# the memory location of a and b is same because they have same value
# variables are different but as their values are same, they are stored in the same memory location,
# and both the variable point to the same memory location

# if we assign a new value to a, it will create a new memory location for a and the memory location of a will be different from b
# if the values are different, then the memory location of the variables will also be different


print(a is b) # checks: are a and b pointing to the same memory location? i.e. id(a) == id(b) ? 
print(a is not b) # checks: are a and b not pointing to the same memory location? i.e. id(a) != id(b)

name1 = "John"

name2 = "John"

print(name1 is name2) # True as both the variables are pointing to the same memory location i.e. id(name1) == id(name2) is True
print(name1 is not name2) # False as both the variables are pointing to the same memory location i.e. id(name1) != id(name2) is False

name3 = "Johny"

print(name1 is name3) # False as both the variables are pointing to different memory location i.e. id(name1) != id(name3) is True
print(name1 is not name3) # True as both the variables are pointing to different memory location i.e. id(name1) != id(name3) is False

print(id(name1))
print(id(name2))
print(id(name3))

# Difference between == operator and is operator
# == operator compares the values of two objects, whereas is operator compares the memory locations of two objects.
# is operator is used to check if two variables point to the same object in memory.
# == operator is used to check if two variables have the same value.
# == is comparison operator and is is identity operator
a = 100 

b = 100 

print(a == b) # in this case, the comparison between is: value of a 100 == value of b 100 is True ie. the values are being compared, not the memory locations

print(a is b) # in this case, the comparison between is: id(a) and id(b) is being compared  ie. the memory locations are being compared, not the values


a = [1, 2, 3, 4, 5]

b = [1, 2, 3, 4, 5] 

print(a == b) # True as the values of a and b are same
print(a is b) # False as the memory locations of a and b are different
'''
in this case, memory is being allocated for variable, the list, and for the values of the list seprately. 

both list has different memory locations. and all the values of the list are sharing the same memory location as the list

i.e. although the ids of the both list are different, the values of the list only initilize once, and being shared 
by the both the list. 

so, id(a) != id(b) but id(a[1]) == id(b[1])  as the values are being shared by both the list

'''
print(id(a))
print(id(b))

print()

print(id(a[1]))
print(id(b[1]))
print(a[1] is b[1]) # True as the values are being shared by both the list and the memory location is same
print(a[1] == b[1]) # True as the values are being shared by both the list and the memory location is same
