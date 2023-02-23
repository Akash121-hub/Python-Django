# Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.


# Python program showing
# how MRO works
 
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
 
# classes ordering
class D(B, C):
    pass
    
r = D()
r.rk()

'''Methods for Method Resolution Order(MRO) of a class: 
To get the method resolution order of a class we can use either __mro__ attribute or mro() method. By using these methods we can display the order in which methods are resolved. For Example'''

# Python program to show the order
# in which methods are resolved
 
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
 
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
 
r = C()
 
# it prints the lookup order
print(C.__mro__)
print(C.mro())

