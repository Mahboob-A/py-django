# python-flow/a-variables.py
# 231224, Monday, 11.30 AM

# how a variable is allocated memory and how it is accessed

# In C/C++, memory is allocated for EACH VARIABLE separately
        # if we have 10 variables, then 10 memory locations are allocated for them
        # if all the variables are same value, still 10 memory locations are allocated for them as there are 10 variables
        # so for C/C++, memory is allowcated variable wise

# In case of Python, memory is allocated for the value of the variable
        # if we have 10 variables, and all the variable has same value, then only 1 memory location is allocated for the value
        # in this case, python will not allocate 10 memory address for the same value which is being used by 10 variables
        # python will only allocated different memory address for the different values
        # as long as the value is same, python will not allocate different memory address for the same value, 
        # and all other varible will point to the same memory address, and until no varible is pointing to the value, 
        # the value will be removed from the memory by the garbage collector
        
        # in C, an Integer takes 4 bytes of memory, and a string takes 1 byte of memory
        # in Python, an Integer takes 28 bytes of memory, and a string takes 49 bytes of memory

        # int a = 20, b = 20 => allowcates different memory address for a and b in C
        # a = 20, b = 20 => allowcates only 1 memory address for 20 in python


# creating multiple variables in one line 
name, age, salary = "John", 25, 50000

print(name), print(age), print(salary)

# assign single value to multiple variables
x = y = z = 50

print(x, y, z)

# variable annotation 
# variable annotation is used to specify the type of the variable
# variable annotation is not used for type checking
# although we can allocate different value to a varialbe other than the type specified in the annotation, but not recommended

name: str = "John"

name = 20 # this is not recommended as we are assigning different type to the variable

print(name)


# Reserved Keywords in Python 

import keyword
print(keyword.kwlist)
print()
print(keyword.softkwlist)
print(keyword.iskeyword("hi"))



