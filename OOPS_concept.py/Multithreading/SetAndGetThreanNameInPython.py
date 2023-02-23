# By default thread names are thread-1 and when you create 2nd thread name is Thread-2

# getName() --> to get the default thread name
# setName(name) --> Used to set the name of thread
# name property --> used to get or set the name of the thread

# Example
from threading import Thread, current_thread

def display():
    current_thread().setName("First Thread") # To set the name
    print("child thread object", current_thread().getName())


t = Thread(target=display)
t.start()

print("main thread",current_thread().getName())
current_thread().name = "Flying thread"
print("main thread",)