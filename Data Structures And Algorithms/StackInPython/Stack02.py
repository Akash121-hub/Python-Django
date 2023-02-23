
from inspect import stack


class Stack:
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit
    
    def push(self,data):
        if len(self.stack) >= self.limit:
            print("Stack is full")
        else:
            self.stack.append(data)
        print(self.stack)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print("Stack is empty")


c_obj = Stack()
c_obj.push(10)
c_obj.push(20)
c_obj.push(30)
c_obj.push(40)
c_obj.push(50)
c_obj.push(60)
c_obj.push(6)
# c_obj.pop(