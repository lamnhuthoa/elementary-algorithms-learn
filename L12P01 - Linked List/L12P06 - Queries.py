# Bai 6
# Queries
class Node:
    def __init__(self, x=0):
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
            
    def delete_head(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
                
    def print_list(self):
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        print(" ".join(result))

n = int(input())
list6 = LinkedList()

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        list6.insert_tail(x)
    elif query[0] == '0':
        list6.delete_head()
        
list6.print_list()