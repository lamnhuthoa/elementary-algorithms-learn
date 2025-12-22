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
        
    def count_full_node(self):
        count = 0
        if self.left is not None and self.right is not None:
            count = 1
        
        if self.left:
            count += self.left.count_full_node()
        if self.right:
            count += self.right.count_full_node()
        return count
        
class BST:
    def __init__(self):
        self.root = None
      
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def count_full_bst(self):
        if self.root is None:
            return 0
        return self.root.count_full_node()
            
            
n = int(input())
a = list(map(int, input().split()))

tree = BST()

for x in a:
    tree.add_to_bst(x)
    
ans = tree.count_full_bst()
print(ans)