# Bai 4
# Insert Index
class Node:
    def __init__(self, x):
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
            
    def prepend_indices(self):
        cur = self.head
        prev = None
        index = 1
        while cur:
            index_node = Node(index)
            index_node.next = cur
            if prev is None:
                self.head = index_node
            else:
                prev.next = index_node
                
            prev = cur
            cur = cur.next
            index += 1
            
    def print_list(self):
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        print(" ".join(result))
        
            
    
list3 = LinkedList()
while True:
    x = int(input())
    if x == 0:
        break
    list3.insert_tail(x)

list3.prepend_indices()
list3.print_list()