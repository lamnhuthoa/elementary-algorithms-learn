# Bai 9
# The Greatest Date
class Node:
    def __init__(self, d=1, m=1, y=1):
        self.day = d
        self.month = m
        self.year = y
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, d, m, y):
        p = Node(d, m, y)
        if not self.head:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
            
    def is_later(self, a, b):
        if a.year != b.year:
            return a.year > b.year
        if a.month != b.month:
            return a.month > b.month
        return a.day > b.day
    
    def find_greatest_date(self):
        if not self.head:
            return None
        cur = self.head
        max_date = self.head
        
        while cur:
            if self.is_later(cur, max_date):
                max_date = cur
            cur = cur.next
        return max_date
    
n = int(input())
lst = LinkedList()
for _ in range(n):
    d, m, y = map(int, input().split())
    lst.insert_tail(d, m, y)

greatest = lst.find_greatest_date()
print(greatest.day, greatest.month, greatest.year)