"""Inheritance is the mechanism to achieve the re-usability of code as one class(child class) can derive the properties of another class(parent class). It also provides transitivity ie. if class C inherits from P then all the sub-classes of C would also inherit from P."""


# Python Program to depict multiple inheritance
# when method is overridden in both classes
 
class Class1:
    def m(self):
        print("In Class1")
       
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3") 
        
class Class4(Class2, Class3):
    pass  
     
obj = Class4()
obj.m()