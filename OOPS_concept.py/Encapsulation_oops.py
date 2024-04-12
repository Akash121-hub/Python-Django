# Encapsulation --> Encapsulation is nothing but the writing the class,The methods process the data available in the variables

# Encapsulation hides variables or some implementation that may be changed so often in a class to prevent outsiders access it directly. They must access it via getter and setter methods.

# Hiding the data for the purpose of production --> Encrypted message or Encrypted email
# Example
class Encpsulation:
    def __init__(self):
        self.id = 10
        self.marks = 100
    
    def display(self):
        print(self.id)
        print(self.marks)

instance_class = Encpsulation()
instance_class.display()

"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.

Although the protected variable can be accessed out of the class as well as in the derived class (modified too in derived class), it is customary(convention not a rule) to not access the protected out the class body.

Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated.

"""
# Python program to
# demonstrate protected members
 
# Creating a base class
class Base:
    def __init__(self,a):
        # Protected member
        self._a = a

class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self,5)
        print("Calling protected member of base class: ",
              self._a)
        
        # Modify the protected variable:
        self._a = 5

        print("Calling modified protected member outside class: ",
              self._a)



obj1 = Derived()
 
obj2 = Base(3)



# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)
 
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)