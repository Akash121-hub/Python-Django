# LINKED LISTS

# Heap memory --> present in RAM and this heap memory allocates the memory dynamically


class Node(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,head):
        self.head = head

    def PrintList(self):
        temp = self.head
        while temp.next == None:
            print(f"{temp.next} -->  end =" " ")
            temp = temp.next
    
    def InsertAtStart(self, data):
        if self.head == None:
            Newnode = Node(data)
            self.head = Newnode
        else:
            Newnode = Node(data)
            Newnode.next = self.head
            self.head = Newnode

    



List = LinkedList()
List.InsertAtStart(20)
List.InsertAtStart(30)
List.InsertAtStart(40)
List.InsertAtStart(50)
List.InsertAtStart(60)
List.PrintList()




    
    