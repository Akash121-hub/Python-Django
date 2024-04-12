# INHERITANCE : --> : Creating the new class from existing classes, so that the new classes will acquire all the features of the existing classes is called INHERITANCE.
"""
Benefits of inheritance are: 
It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Inheritance offers a simple, understandable model structure. 
Less development and maintenance expenses result from an inheritance. 

"""

class A:
    a = 1
    b = 2

    def method1(cls):
        print(cls.a)
        print(cls.b)

class B(A):
    c = 3
    def method2(cls):
        print(cls.c + cls.a)

m = B()
m.method2()


# Inheritance examples
# A Python program to demonstrate inheritance
class Person(object):
    # Constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id

  # To check if this person is an employee
    def Display(self):
        print(self.name,self.id)

    
    def CheckEmployee(self):
        employee_ids = [1,2,3,4,5,6,7,10541]
        if self.id not in employee_ids:
            print("Not an employee")
        else:
            print("Employee is present")
        

# Creating a Child Class
# Here Emp is another class which is going to inherit the properties of the Person class(base class).

class Emp(Person):

    def Print(self):
        print("calling Emp class")

emp_details = Emp("Akash",10541)

# calling parent class function
emp_details.Display()


# Calling child class function
emp_details.Print()

emp_details.CheckEmployee()

class D:
    def __init__(self, n='Rahul'):
        self.name = n
 
 
class B(D):
    def __init__(self, roll,n):
        self.roll = roll

        D.__init__(self,n)
 
 
object = B("23",1)
print(object.name)

