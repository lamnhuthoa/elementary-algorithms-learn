# Bai 8 
# Palindrome number
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

    def is_palindrome(self, num):
        s = str(num)
        return s == s[::-1]  # reversed string
    
    def print_palindrome_indices(self):
        cur = self.head
        index = 0
        result = []
        while cur:
            if self.is_palindrome(cur.data):
                result.append(str(index))
            cur = cur.next
            index += 1
        print(" ".join(result))

lst = LinkedList()
while True:
    n = int(input())
    if n == -1:
        break
    lst.insert_tail(n)

lst.print_palindrome_indices()