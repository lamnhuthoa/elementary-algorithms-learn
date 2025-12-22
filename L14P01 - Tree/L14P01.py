class Node:
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right
        
    def add_to_node(self, x):
        if x < self.data:
            if (self.left == None):
                p = Node(x)
                self.left = p
            else:
                self.left.add_to_node(x)
        elif x > self.data:
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
        
    def print_in_order_node(self):
        if self.left != None:
            self.left.print_in_order_node()
            
        print(self.data, end=" ")

        if self.right != None:
            self.right.print_in_order_node()
            
    def get_height_node(self):
        if self.left != None:
            hL = self.left.get_height_node()
        if self.right != None:
            hR = self.right.get_height_node()
        
        height = 1 + max(hL, hR)
        return height
    
    def sum_leaf_node(self):
        if self.left is None and self.right is None:
            return self.data
        
        sum_left = self.left.sum_leaf_node() if self.left else 0
        sum_right = self.right.sum_leaf_node() if self.right else 0
    
        return sum_left + sum_right
        
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
            
    def min_bst(self):
        return self.root.min_node()
    
    def print_in_order_bst(self):
        self.root.print_in_order_node()
        
    def get_height_bst(self):
        return self.root.get_height_node()
    
    def sum_leaf_bst(self):
        return self.root.sum_leaf_node()
    
    def count_full_bst(self):
        if self.root is None:
            return 0
        return self.root.count_full_node()