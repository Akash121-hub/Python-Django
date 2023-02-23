# Decorators --> Decoraters allows you to wrap your (decorator) function in another function
# very powerful tool of python

# Exapmle decorator function
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took "+ str((start-end)*1000) +" milisecond   ")
        return result
    return wrapper

@calculate_time
def cla_sqr(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

print(cla_sqr([1,2,3,4,5,6,7,8]))


def upper_func():
    message = "HI"
    def wrapper():
        print(message)
    return wrapper

s = upper_func()
print(s)
s()
s()

def deco(func):
    def wrapper(a,b):
        result = func(a,b)
        if b > a:
            temp = a
            a = b
            b = temp
            print("Decorator executed")
            print("a val ",a)
            print(b)
        else:
            print("Decorator executed")
            a = a
            b = b
            
        return result
    return wrapper


@deco
def div(a,b):
    return a/b

a1 = 20
b1 = 10

print(div(a1,b1))



def modify_func(func):
    def inner_func():
        print("This is inner function before modifying the original func")
        func(2,3)
        print("This is inner function after modifying the original func")
    
    return inner_func

@modify_func
def original_func(a,b):
    print("This is original function")
    print("Created this func at beginning")
    return a + b
original_func()


def decor(fun):
    def inner():
        res = fun()
        add = res + 5
        return add
    return inner


@decor
def add():
    return 10

print(add())

