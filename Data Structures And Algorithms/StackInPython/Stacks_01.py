# STACKS --> :  Stacks are the group of element stored in LIFO ( Last In First Out ) Order. This means that the element which
# are stored in stack will be the first element to removed from stack.

# 1. Inserting elements into stack is called PUSH operation.

# 2. Removing elements from stack is called pop operation.

# 3. Searching element from the stack and rerutning it without removing it from the stack is called PEEP operation.

# 4. Insertion and deletion of elements take place only from one side of the stack is called 'top' of the stack. the other side of the stack is called 'bottom' which is closed and thus does not allow any operations.


# Python provides list data types that can be used to create stacks. we should first create a first      stack class with the following operations

# OPERATIONS -- > "PUSH", "POP", "PEEP", "SEARCHING", "EMPTY OR NOT" 

# *** WRITE A PYTHON PROGRAM TO CREATE A STACK CLASS THAT CAN PERFORM SOME IMPORTANT OPERATIONS *** #


class Stack:
    def __init__(self):
        self.stck = []
    
    def push(self,element):
        self.stck.append(element)
    
    def pop(self):
        self.stck.pop()

    # def search(self):
        