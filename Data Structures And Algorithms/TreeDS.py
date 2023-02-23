# what is Gneral Tree data structure  
    # Hierarchical form and it's recursive data structure

# EXAMPLE :         ELECTRONICS --> ROOT NODE
                # TELEVISION     CELLPHONES      LAPTOPS   --> PARENT NODE
            # SAMSUNG PHILIPS   IPHONE REDMI    DELL HP  --> CHILD NODE


class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        if self.

def build_product_tree():
    root = Tree("ELECTRONICS")
    laptop = Tree("LAPTOP")
    root.add_child(laptop)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    pass