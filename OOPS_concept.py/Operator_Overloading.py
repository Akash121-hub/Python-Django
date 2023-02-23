"""Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. """

'''When we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined. There by changing this magic method’s code, we can give extra meaning to the + operator. '''


class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
 
print(ob1 + ob2)
print(ob3 + ob4)


class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return self.a + other.a,self.b + other.b

obj = Complex(8,9)
obj1 = Complex(4,5)
obj2 = obj+obj1
# print(type(obj2))
print(obj2)