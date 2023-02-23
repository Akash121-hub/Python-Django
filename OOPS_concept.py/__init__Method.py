'''                     __init__
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created. Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.'''
# Python program to
# demonstrate init with
# inheritance
  
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
          
  
class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something
          
obj = B("Something")