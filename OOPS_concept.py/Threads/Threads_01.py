# find the current running thread
import threading
print("let us find the current thread ")

print(" currently running thread is : ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print(" Main thread is running  ")
else:
    print(" Not running main thread ")