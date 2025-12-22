# Find Min
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
            # 0 -> 1
            self.head = p
            self.tail = p
        else:
            # 1 -> 2 -> 3 -> 4
            self.tail.next = p
            self.tail = p
            
    def min(self):
        # assume list has at least 1 element
        cur = self.head
        min_node = cur
        while cur is not None:
            if cur.data < min_node.data:
                min_node = cur
            cur = cur.next
        return min_node
        
        
list1 = LinkedList()
while True:
    x = int(input())
    if x == 0:
        break
    list1.insert_tail(x)

ans = list1.min()
print(ans.data)