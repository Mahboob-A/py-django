# recap some basic python
# 130125, monday, 08.30 am
# https://realpython.com/python-scope-legb-rule/

import http, math
import builtins 

# the globals tells us what is in the global scope of this current file
def print_global_scope(): 
        print(globals())
        print()        

# print_global_scope()

# if we want to know what a module offers, or the scope of the module, we
# can use the dir() function or the __dict__ attribute.
def print_what_a_module_has(): 
        print(dir(http))
        print()
        print(dir(math))

        print(math.__dict__)

        print(math.__doc__)

        print(math.__dict__.keys())


def see_what_a_function_has(name=None):
        name2 = "doe"
        age = 30 
        print("name: ", name + " ", name2, "\nage: ", age)

# see_what_a_function_has(name="john")
# using __code__.co_ we can inspect the scope, names, args etc of a function
# print(see_what_a_function_has.__code__)
print(see_what_a_function_has.__code__.co_varnames)
print(see_what_a_function_has.__code__.co_code)
print(see_what_a_function_has.__code__.co_argcount)
print(see_what_a_function_has.__code__.co_name)
print(see_what_a_function_has.__code__.co_names)

print(see_what_a_function_has.__code__.co_filename)

# print(dir(see_what_a_function_has))

# print("\n\n")
# print(dir(builtins))


# the regular for loops, the loop variable holds the last value processed by the loop after the loop ended.
for item in range(1, 6):
        print(item)

print()
print(item)        
