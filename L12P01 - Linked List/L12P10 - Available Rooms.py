# Bai 10
# Available Rooms
class Node:
    def __init__(self, room_id="", price=0, available=0):
        self.room_id = room_id
        self.price = price
        self.available = available
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, room_id, price, available):
        p = Node(room_id, price, available)
        if not self.head:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def print_available_rooms(self):
        cur = self.head
        while cur:
            if cur.available == 0:
                print(cur.room_id, cur.price)
            cur = cur.next

n = int(input())
lst = LinkedList()

for _ in range(n):
    room_id, price, avail = input().split()
    lst.insert_tail(room_id, int(price), int(avail))

lst.print_available_rooms()