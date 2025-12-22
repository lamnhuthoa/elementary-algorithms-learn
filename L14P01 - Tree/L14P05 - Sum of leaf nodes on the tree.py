class Node:
    def __init__(self, x=0, left = None, right=None):
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
        
    def sum_leaf_node(self):
        if self.left is None and self.right is None:
            return self.data
        
        sum_left = self.left.sum_leaf_node() if self.left else 0
        sum_right = self.right.sum_leaf_node() if self.right else 0
    
        return sum_left + sum_right
        
class BST:
    def __init__(self):
        self.root = None
      
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def sum_leaf_bst(self):
        return self.root.sum_leaf_node()
            
            
n = int(input())
a = list(map(int, input().split()))

tree = BST()

for x in a:
    tree.add_to_bst(x)
    
ans = tree.sum_leaf_bst()
print(ans)