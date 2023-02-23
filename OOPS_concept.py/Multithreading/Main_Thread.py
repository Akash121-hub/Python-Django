# Main Thread: when we start the program, one thread begins runnign immediately which is called main thread of that program created by PVM

# Test program for thread

import threading

t = threading.current_thread().getName()

print("Akash SHinde")

print(t)