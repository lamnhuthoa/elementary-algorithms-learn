# Bai 2
# Under Average
class Node:
    def __init__(self, x=0.0):
        self.data = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_tail(self, x):
        p = Node(x)
        if self.head is None:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
            
    def print_under_average(self):
        cur = self.head
        while cur is not None:
            if cur.data < 5.0:
                if cur.data.is_integer():
                    print(int(cur.data))
                else:
                    print(cur.data)
            cur = cur.next
            
lst = LinkedList()
while True:
    n = float(input())
    if n == -1:
        break
    lst.insert_tail(n)
    
lst.print_under_average()