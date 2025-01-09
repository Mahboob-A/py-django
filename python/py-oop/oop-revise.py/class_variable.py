# 050524, Sunday, 01.00 pm


# how class varialbe reacts: change through the class and change through the instance
class HTMLDoc:
    extention = "html"
    extra = None
    version = 5


htmldoc = HTMLDoc()
htmldoc2 = HTMLDoc()
htmldoc3 = HTMLDoc()

# changing the class variable using an instance
htmldoc.extention = ".html"

# settings the class varialbe using the class # from .html to  html5
setattr(HTMLDoc, "extention", "html5")

# get the class variables using the instance
extention = getattr(htmldoc, "extention")
extra = getattr(htmldoc, "extra")
version = getattr(htmldoc, "version")

print("extention: ", extention)  # .html
print("version: ", version)  # 5
print("extra: ", extra)  # None

# get the class variable using another instance (this instance dit not change the class varibles like the first one)
print()
extention2 = getattr(htmldoc2, "extention")
print("extention2: ", extention2)  # html5

# get the class varialbes again using the first instance which initially changed the class variable
print()
extention = getattr(htmldoc, "extention")
print("extention: ", extention)  # .html

# now change the class variable again using the first instance
setattr(htmldoc, "extention", "html-5.1")
print()
extention = getattr(htmldoc, "extention")
print("extention: ", extention)  # html-5.1


# now get the class varialbe using the class
print()
extention = getattr(HTMLDoc, "extention")
print("extention: ", extention)  # html5

# now change the class varible using the second instance and get the value
print()
setattr(htmldoc2, "extention", "new-html")
# the get value
extention2 = getattr(htmldoc2, "extention")
print("extention2: ", extention2)  # new-html

# again access the class varialbe using the 1st instance
print()
extention = getattr(htmldoc, "extention")
print("extention of 1st instance: ", extention)  # html-5.1

# now again get the class varialbe using the class
print()
extention = getattr(HTMLDoc, "extention")
print("extention: ", extention)  # html5

# as htmldoc3 instance has not change the class varialbe at all, it is getting the original class variable value
print()
extention3 = getattr(htmldoc3, "extention")
print("extention 3: ", extention3)

print("\n\n")
print("class dir: ", HTMLDoc.__dir__)
print("class dict: ", HTMLDoc.__dict__)
print()
print("dir of instance 1: ", htmldoc.__dir__)
print("dict of instance 1: ", htmldoc.__dict__)
print()
print("dir of instance 2: ", htmldoc2.__dir__)
print("dict of instance 2: ", htmldoc2.__dict__)
print()
print("dir of instance 3: ", htmldoc3.__dir__)
print("dict of instance 3: ", htmldoc3.__dict__)


"""
Key Takeaway: 

Changing class varialbe data: 

so, whenever we change a class variable using an instance, then a new instance variable 
exclusive to that instance with the class variable with the updated value is created. 

hence, the original class varialbe remains same. 
but a new instance varialbe to that instance is created. 

so, to change a class variable always change wich class, 
otherwise if changed with an instance, then the change will not reflect on other instances, 
but a instance variable for that instance will be created. 

"""
