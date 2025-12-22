# Fibonacci Linked List
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
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def insert_fibonacci(self, x, y, n):
        if n == 0:
            return

        a = x
        b = y

        self.insert_tail(a)
        if n == 1:
            return

        self.insert_tail(b)
        if n == 2:
            return

        for i in range(2, n): 
            next_fib = (a + b) % 1_000_007
            self.insert_tail(next_fib)
            a, b = b, next_fib

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        
  
x, y, n = map(int, input().split())
lst = LinkedList()
lst.insert_fibonacci(x, y, n)
lst.print_list()
