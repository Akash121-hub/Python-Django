from threading import Thread


class ChildClass(Thread):
    def run(self):
        # print("Run method") # Over riding the run method
        for i in range(5):
            print("Child Method")


Thread_obj = ChildClass()
Thread_obj.start()
print(Thread_obj.getName())

# run() --> Every thread will run this method when thread is started

# join() --> This method is used to wait till the thread is completely executes the run() method.


# Thread Child Class with Constructor ( Implement Constructor in child class)

class MyThread(Thread):
    def __init__(self,a):
        Thread.__init__(self) # start the parent class constructor is must
        self.a = a
t = MyThread()
t.start()


# creating a thread without creating a child class to Thread class
   # We can create an independent thread child class that does not inherit from Thread class from threading module

class MyClass:
    pass

obj_name = MyClass()

# Syntax
# Thread_object = Thread(target=obj_name.function_name,args=(arg1,arg2))
