class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right
        
    def add_to_node(self, x):
        if x < self.data:
            if self.left == None:
                p = Node(x)
                self.left = p
            else:
                self.left.add_to_node(x)
        elif x > self.data:
            if self.right == None:
                p = Node(x)
                self.right = p
            else:
                self.right.add_to_node(x)
        else:
            return
        
    def get_height_node(self):
        hL = self.left.get_height_node() if self.left else 0
        hR = self.right.get_height_node() if self.right else 0
            
        height = 1 + max(hL, hR)
        return height
        
        
class BST:
    def __init__(self):
        self.root = None
        
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def get_height_bst(self):
        return self.root.get_height_node()
    
    
n = int(input())
a = list(map(int, input().split()))

tree = BST()

for x in a:
    tree.add_to_bst(x)
    
ans = tree.get_height_bst()
print(ans)