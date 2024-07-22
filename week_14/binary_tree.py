
class BinaryTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinaryTree(data)
            else:
                self.right.insert(data)
    
    def print_in_traversal(self):
        if self.left:
            self.left.print_in_traversal()
        print(self.data)
        if self.right:
            self.right.print_in_traversal()
    
    def print_pre_traversal(self):
        print(self.data)
        if self.left:
            self.left.print_pre_traversal()
        if self.right:
            self.right.print_pre_traversal()

    def print_post_traversal(self,):
        
        if self.left:
            self.left.print_post_traversal()
        if self.right:
            self.right.print_post_traversal()  
        print(self.data)    
    

tree =  BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)



print("In-order Traversal:")
tree.print_in_traversal()
print("\nPre-order Traversal:")
tree.print_pre_traversal()
print("\nPost-order Traversal:")
tree.print_post_traversal()



