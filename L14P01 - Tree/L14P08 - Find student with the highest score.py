'''
Find student with the highest score
'''
class Node:
    def __init__(self, student):
        self.student = student 
        self.left = None
        self.right = None
      
    def add_to_node(self, student):
        if student[2] < self.student[2]: # Compare scores
            if self.left is None:
                self.left = Node(student)
            else:
                self.left.add_to_node(student)
        elif student[2] > self.student[2]:
            if self.right is None:
                self.right = Node(student)
            else:
                self.right.add_to_node(student)
        else:
            return
        
    def find_highest_score_student_node(self):
        if self.right is None:
            return self.student
        else:
            return self.right.find_highest_score_student_node()
    
        
        
class BST:
    def __init__(self):
        self.root = None
      
    def add_to_bst(self, x):
        if self.root == None:
            p = Node(x)
            self.root = p
        else:
            self.root.add_to_node(x)
            
    def find_highest_score_student_bst(self):
        if self.root is None:
            return None
        return self.root.find_highest_score_student_node()
            
            
n = int(input())
tree = BST()

for _ in range(n):
    parts = input().split()
    StudentID = parts[0]
    Name = " ".join(parts[1:-1])
    Grade = float(parts[-1])
    student = (StudentID, Name, Grade)
    tree.add_to_bst(student)
    
highest = tree.find_highest_score_student_bst()
if highest:
    print(f"{highest[0]} {highest[1]} {highest[2]}")