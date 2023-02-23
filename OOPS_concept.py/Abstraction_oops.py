
"""An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class."""
# Abstraction: --> Abstraction is to expose only that data if interest to the user.This is called ABSTRACTION.

# Example: -

# A Car will have some parts like engine, radiator, battery, mechanical and electrical equipment etc

# CODE EXAMPLE 

class Myclass:
    def __init__(self):
        self.__y = 10 # Y is PRIVATE VARIABLE
        self.x = 20 # X is Loacal variable

m = Myclass()
print(m._Myclass__y)   # This is the way to display the private variable

# *** We have used underscore before the classname and two underscores after the classname. Like ths we are using the names differently to access the classname this is called the name MANGLING. ***


print(m.x) # Way to display the local variable
