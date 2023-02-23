# Linked Lists: --> : These are the lists contains groups of elements. Each node will have three fields
# 1. The data filed that contains data
# 2. Link Field that contains refrence to the previous field ( Link filed store refrences i.e. memory locations  )
# 3. Another link field that contains refrence to the next node

# ***   Python Lists are used to implement the Linked lists *** #

# The Genereal OPERATIONS are performed on linked lists.

    # 1. Traversing the linked list 
    # 2. Appending elements to the linked lists
    # 3. Inserting elements in the linked lists
    # 4. Removing elements the linked lists
    # 5. Replacing elements the linked lists
    # 6. Searcing for an element location the linked lists
    # 7. Size of the the linked lists

# wirte a program to create linked list and perform operations on it

'''
linked_list = []
linked_list.append("India")
linked_list.append("America")
linked_list.append("United Kingdom")
print("the existing list",linked_list)
choice = 0

while choice < 5:
    print("Linked list Operations")
    print("1 to add element")
    print("2 to remove element")
    print("3 to replace element")
    print("4 to search for element")
    print("5 to exits")
    choice = int(input("enter no:  "))

    if choice == 1:
        add_element = input("Enter element to add:   ")
        linked_list.append(add_element)
    elif choice == 2:
        rm_element = input("Enter element to remove:  ")
        linked_list.remove(rm_element)
    elif choice == 3:
        enter_index = int(input("enter element index: "))
        replace_element = input("enter element ot replace:  ")
        linked_list.insert(enter_index,replace_element)
    elif choice == 4:
        index_search = input("enter element to search index  ")
        try:
            
            pos = linked_list.index(index_search)
            print("Your element position is ", pos)
        except ValueError:
            print("Value not found")
    else:
        break
    print(linked_list)      '''


# Linked Lists Benefits
# 1. You don't need to pre-allocate the space
# 2. Insertion and Deletion is easier
# 3. Memory management is more efficient as compared to lists
# 4. Randomly stored 
# 5. Linked Lists are used to create Stacks and Queues

# **** Single Linked List --> You will have link to your next node **** #

# **** Double Linked List --> You will have link to your previous and next node **** #



                             ###### DEQUE #####
# Queue (FIFO)--> First in first out data type. Example:- Restaurant Queue

# Stacks (LIFO) --> Last In First out

from collections import deque

lnkd_lst = deque()

'''
queue = deque()

# Implementing Queue (FIFO) --> First in First Out
for i in range(0,6):
    queue.append(i)
    print(queue)

for i in range(len(queue)):
    queue.popleft()
    print(queue) '''

#############################################


# Implementing Stacks (LIFO)--> Last In First Out

'''
stack = deque()

for i in range(0,6):
    stack.appendleft(i)
    print(stack)


for i in range(len(stack)):
    stack.pop()
    print(stack)
 

'''

###################################################


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("my linked list is empty")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count


    def remove_at_index(self, index):
        if index <0 or index >= self.get_length():
            raise exception ("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise exception ("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['a','b','s','h','l'])
    print(ll.get_length())
    print(ll.insert_at(2,'Jack fruit'))
    # print(ll.remove_at_index(2))
    ll.print()
    print(type(ll))
    
