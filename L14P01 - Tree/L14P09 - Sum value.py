class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
    def add_to_node(self, x):
        if x < self.data:
            if self.left is None:
                self.left = Node(x)
            else:
                self.left.add_to_node(x)
        elif x > self.data:
            if self.right is None:
                self.right = Node(x)
            else:
                self.right.add_to_node(x)
                
    def sum_less_than_x(self, x):
        total = 0
        if self.left:
            total += self.left.sum_less_than_x(x)
            
        if self.data < x:
            total += self.data
            
        if self.right:
            total += self.right.sum_less_than_x(x)
            
        return total
            
        
class BST:
    def __init__(self):
        self.root = None

    def add_to_bst(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.root.add_to_node(x)

    def sum_less_than(self, x):
        if self.root is None:
            return 0
        return self.root.sum_less_than_x(x)

n, x = map(int, input().split())
a = list(map(int, input().split()))

tree = BST()
for val in a:
    tree.add_to_bst(val)

print(tree.sum_less_than(x))