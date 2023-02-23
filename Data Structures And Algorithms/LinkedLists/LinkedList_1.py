# Linked Lists

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def DeleteFirst(self):
        if self.start == None:
            print("Linked List is empty")
        else:
            self.start = self.start.next

    def Traverse(self):
        if self.start == None:
            print("Linked List is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end= ' ')
                temp = temp.next


    def InsertAtLast(self,value):
        newNode = node(value)
        
        if (self.start ==  None):
            self.start = newNode
        else:
            tmp = self.start
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = newNode



# PRACTICE 
        
class nodes:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.start = None
    
    def DeleteFirst(self):
        if self.start == None:
            print("Linked List is empty")
        else:
            self.start = self.start.next
        