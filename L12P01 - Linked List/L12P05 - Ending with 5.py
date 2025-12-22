# Bai 5
# Ending with "5"
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
            
    def check_ending_with_5(self, val):
        return abs(val) % 10 == 5

    def remove_ending_with_5(self):
        if self.head == None:
            return
        
        while self.head and self.check_ending_with_5(self.head.data):
            self.head = self.head.next

        cur = self.head
        while cur and cur.next:
            if self.check_ending_with_5(cur.next.data):
                cur.next = cur.next.next
            else:
                cur = cur.next

    def print_list(self):
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        print(" ".join(result))


n = int(input())
list5 = LinkedList()
for _ in range(n):
    x = int(input())
    list5.insert_tail(x)

list5.remove_ending_with_5()

list5.print_list()