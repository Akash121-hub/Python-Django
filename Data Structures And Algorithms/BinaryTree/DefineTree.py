# 1. define a binary tree
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    #2. below we have to define a function that can add a node to the tree or adding a node
    # define the recursive insert function
    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

# 4. printing all nodes Inordertraversal
def InorderTraversal(r):
    if r is None:
        return
    else:
        InorderTraversal(r.left)
        print(r.data)
        InorderTraversal(r.right)

# 5. printing all nodes in preorder traversal

def PreOrderTravelsal(r):
    if r is None:
        return
    else:
        print(r.data, end = ' ')
        PreOrderTravelsal(r.left)
        PreOrderTravelsal(r.right)
        
if __name__ == "__main__":
    # building up a tree
    root = Node("g")
    root.insert('a')
    root.insert('r')
    root.insert('t')
    root.insert('e')
    root.insert('w')
    root.insert('p')
    print("hello")

PreOrderTravelsal(root)

# 4. printing all nodes 
