class Node:
    def __init__(self, x=-1):
        self.data = x
        self.next = None
        
class LinkedList:
    head: Node
    tail: Node
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, x):
        p = Node(x)
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
            
            
list1 = LinkedList()
while True:
    x = int(input())
    if x == -1:
        break
    list1.insert_tail(x)
    

list2 = LinkedList()
while True:
    x = int(input())
    if x == -1:
        break
    list2.insert_tail(x)
    
s1 = set()
p = list1.head
while p:
    s1.add(p.data)
    p = p.next
    
intersection_set = set()
p = list2.head
while p:
    if p.data in s1:
        intersection_set.add(p.data)
    p = p.next
    
if intersection_set:
    print(" ".join(map(str, intersection_set)))
else:
    print("NO INTERSECTION")