# Bai 7
# The Second Largest Number
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
        if not self.head:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def find_second_largest(self):
        if not self.head or not self.head.next:
            return -1
        
        first = second = float('-inf')
        cur = self.head
        while cur:
            val = cur.data
            if val > first:
                second = first
                first = val
            elif first > val > second:
                second = val
            cur = cur.next
            
        if second == float('-inf'):
            return -1
        return second
    
lst = LinkedList()
while True:
    x = float(input())
    if x == -1:
        break
    lst.insert_tail(x)

result = lst.find_second_largest()
print(result)