# Bai 3
# Prim numbers in linked list
def is_prime(x) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

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
            
    def count_prime_numbers(self) -> None:
        cur = self.head
        count = 0
        while cur is not None:
            if is_prime(cur.data):
                count += 1
            cur = cur.next
        print(count)
        
lst2 = LinkedList()
while True:
    n = int(input())
    if n == -1:
        break
    lst2.insert_tail(n)
    
lst2.count_prime_numbers()