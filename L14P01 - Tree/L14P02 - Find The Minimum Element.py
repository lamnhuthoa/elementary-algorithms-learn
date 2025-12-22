# Bai 1
# Find the minimum element
class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right
        
    def add_to_node(self, x):
        if (x < self.data):
            if (self.left == None):
                p = Node(x)
                self.left = p
            else:
                self.left.add_to_node(x)
        elif (x > self.data):
            if (self.right == None):
                p = Node(x)
                self.right = p
            else:
                self.right.add_to_node(x)
        else:
            return
        
    def min_node(self):
        if self.left == None:
            return self.data
        else:
            return self.left.min_node()
    
class BST:
    def __init__(self):
        self.root = None
        
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def min_bst(self):
        return self.root.min_node()
    
n = int(input())
a = list(map(int, input().split()))

tree = BST()

for x in a:
    tree.add_to_bst(x)
    
ans = tree.min_bst()
print(ans)