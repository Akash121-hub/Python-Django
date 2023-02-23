# creating our new thread we need object of Thread class
# Creating a thread without using a class
# creating a child class by using Thread classs
# syntax

from threading import Thread

# thread_obj = Thread(target=function_name,args=(arg1,arg2))
# args --> tuple

# How to start thread --> by calling start() Method

def display(a):
    print("Thread running", a)

t = Thread(target=display,args=(10,))
t.start()



