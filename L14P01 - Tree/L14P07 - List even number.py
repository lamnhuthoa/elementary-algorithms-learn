'''
Problem: List Even Numbers in a Binary Search Tree

Statement
Given N numbers, construct a binary search tree (BST) from these elements.
Using post-order traversal, print all even numbers in the BST in one line.

Input Format
The first line contains an integer N — the number of elements in the BST 0 ≤ N ≤ 10^3
The second line contains N integers, each with absolute value ≤ 10^6.

Output Format
Print all even numbers in the BST using **post-order** traversal, separated by spaces, in a single line.
'''
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
        
    def list_even_number_node(self):
        if self.left:
            self.left.list_even_number_node()
        if self.right:
            self.right.list_even_number_node()
        if self.data % 2 == 0:
            print(self.data, end=" ")
        
        
class BST:
    def __init__(self):
        self.root = None
      
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def list_even_number_bst(self):
        if self.root:
            self.root.list_even_number_node()
            
            
n = int(input())
a = list(map(int, input().split()))

tree = BST()

for x in a:
    tree.add_to_bst(x)
    
tree.list_even_number_bst()