# Bai 4
# Create list
'''
You are given an integer linked list. Please build a new linked list from given linked list with following rules:
- First node in new linked list is first node in given linked list.
- i(th) node in new linked list contains the sum of i(th) node and node before i(th) node in given linked list.
Print new list.

Input:
- The first line is number of elements in given linked list N
- The second line contains N integers in given linked list with absolute value not exceeding 10**6
Output:
A single line is elements in new linked list built following above rules, each integer is separated by a single space.
'''
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
            
    def build_new_list(self):
        new_list = LinkedList()
        if self.head is None:
            return new_list
        
        curr = self.head
        new_list.insert_tail(curr.data)
        prev_data = curr.data
        curr = curr.next
        
        while curr:
            new_value = prev_data + curr.data
            new_list.insert_tail(new_value)
            prev_data = curr.data
            curr = curr.next
        return new_list
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
            
n = int(input())
values = list(map(int, input().split()))
linked_list = LinkedList()
for value in values:
    linked_list.insert_tail(value)
    
new_linked_list = linked_list.build_new_list()
new_linked_list.print_list()