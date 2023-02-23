"""
The queue data structure aslo means the same where the data elements are arranged in a queue. The uniqueness of queue lies in the way items are added and removed. The items are allowed at on end but removed form the other end. So it is a First-in-First out method.
A queue can be implemented using python list where we can use the insert() and pop() methods to add and remove elements. Their is no insertion as data elements are always added at the end of the queue.
"""

from doctest import FAIL_FAST


class Queue:
    def __init__(self):
        self.queue = list()

    def add_elem(self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove_elem(self):
        if len(self.queue) > 0:
            self.queue.pop()
            return ("Item removed")
        return ("Queue is empty")


obj = Queue()
obj.add_elem("AKASH")
print(obj.remove_elem())
print(obj.remove_elem())
