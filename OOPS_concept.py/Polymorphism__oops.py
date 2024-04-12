# Polymorphism -- > : If the object or method exhibiting different behaviour in different context, it is called polymorphic nature

'''
# What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

# Example of inbuilt polymorphic functions:

'''


# Python program to demonstrate in-built poly-
# morphic functions
 
# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))


# Examples of user-defined polymorphic functions: 

def add(x, y, z = 0):
    return x + y+z
 
# Driver code
print(add(2, 3))
print(add(2, 3, 4))


# Polymorphism with class methods: 


class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")

# Polymorphism with class methods: 

# The below code shows how Python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()


