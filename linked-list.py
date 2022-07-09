"""
Design a singly linked list class that has a head and tail. Every node is to have
two attributes: value: the value of the current node, and next: a pointer to the next
node. The linke list is to be 0-indexed. The class should support the following:
- SinglyLinkeList() Initializes the SinglyLinkeList object
- get(indx) Get the value of the index(th) node. If the index is invalid, return -1
- addAtHead(vlaue) - Add a node of give value before the first element of the linked list
- addAtTail(value) - Add a node of given value before the index(th) node in the linked
    list. if index equals the length of the linked list, the node will be appended to
    the end of the linked list. If index is greater than the lenght, don't insert the node
- deleteAtIndex(index) - Delete the index(th) node in the linked list. If the index is 
    valid, else nothing happens
"""


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # use to track the size of the linked list
    
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current


    def add_at_head(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return self

    def add_at_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            self.tail = node 
        self.size += 1
        return self


    def add_at_index(self, value, index):
        if index < 0 or index > self.size:
            return 'Invalid index'
        if index == self.size:
            return self.add_at_tail(value)
        if index == 0:
            return self.add_at_head(value)
        node = Node(value)
        prev = self.get(index-1)
        temp = prev.next
        prev.next = node 
        node.next = temp
        self.size += 1
        return self
    
    def delete_at_index(self, index):
        if index < 0 or index > self.size:
            return 'invalid index'
        # return the node that we are deleting
        if index == 0:
            # delete head
            temp = self.head
            self.head = temp.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp 
        if index == self.size-1:
            # delete tail
            old_tail = self.tail
            new_tail = self.get(index-1)
            self.tail = new_tail
            new_tail.next = None 
            self.size -= 1
            # no need to check if size = 0 as it has been taken careof earlier
            return old_tail
        else:
            # delete another node
            prev = self.get(index-1)
            deleted_node = prev.next
            prev.next = deleted_node.next
            self.size -= 1
            return deleted_node
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        
sl = Singly_Linked_List()
sl.add_at_head(1)
sl.add_at_head(2)
sl.add_at_tail(3)
sl.add_at_index(2, 3)
print(sl.print_list())


"""
You are given the head of a Sorted Singly Linked list. Write a function that will 
take the given head as input, delete all nodes that have a value that is already
the value of another node so that each value appears 1 time only and return the 
linked list, which is still to be a sorted linked list
"""
# create some entries into a linked list called head
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')


def delete_duplicates(head):
    current = head
    while current:
        next_distinct_value = current.next
        while next_distinct_value != None and current.value == next_distinct_value.value:
            next_distinct_value = next_distinct_value.next
        current.next = next_distinct_value
        current = next_distinct_value       
    return head

def print_list(node):
        current = head
        while current is not None:
            print(current.value, end=" ")
            current = current.next

print_list(delete_duplicates(head))


"""
Reverse SLL: You are given a head of a Singly Linked List. Write a function that will
take the given head as input, reverse the Linked List and return the new head of the
reversed Linked List.
"""
# store some values in the singly linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next = current.next 
        current.next = prev
        prev = current
        current = next 
    return prev 

print_list(reverse_linked_list(head))


"""
Tortise and Hare: You are given the head of alinked list. Check if there is a cycle
and if yes, return the node where the cycle begins. If there is no cycle, return null
There is a cycle in a linked list if there is some node inthe list that can be reached
again by continuously following the next pointer. Do not modify the linked list
"""
def checkloop(head):
    if not head:
        return None
    if not head.next:
        return None 
    
    hare = head
    tortoise = head
    while hare and hare.next:  # while there is a node and no null
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:  # when they meet, it means that there is a loop
            break
    if hare != tortoise:  # if the reason for breakout is not hare = tortoise
        return None
        # find where the cycle begins
    pointer = head
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
    return tortoise


# input values to the linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six 
# make a loop
six.next = two 

head = one

print(checkloop(head))


"""
Given an array of integers nums containing n+1 integers where each integer is in the 
range [1, n] inclusive. There is only one repeated number in nums, return this repeated
number. You must solve the problem without modifying the array nums and use only constant
extra space
"""
def get_duplicate(nums):
    tortoise = 0
    hare = 0

    while True:
        hare = nums[nums[hare]] # moves 2 spaces at a time
        tortoise = nums[tortoise] # moves a single space

        if hare == tortoise:
            pointer = 0
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]
            return pointer


"""
You are give two non-empty linked lists representing two non-negative integers. The 
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list. You may assume the two numbers
do not contain anyleading zero, except the number 0 itself. 0<=Node value<=9
"""
def add_2_numbers(l1, l2):
    carry_forward = 0
    results = Singly_Linked_List()
    while l1 or l2 or carry_forward:
        l1_value = l1.value if l1 else 0  #conditional operator
        l2_value = l2.value if l2 else 0
        sum_ = l1_value + l2_value + carry_forward
        node_value_in_result = sum_ % 10
        #print(f'node value: {node_value_in_result}')
        results.add_at_tail(node_value_in_result)
        carry_forward = sum_ // 10
        #print(f'carry forward: {carry_forward}')
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return results

l1 = Singly_Linked_List()
l2 = Singly_Linked_List()
# 540 + 723 = 1263
l1.add_at_tail(0)
l1.add_at_tail(4)
l1.add_at_tail(5)

l2.add_at_tail(3)
l2.add_at_tail(2)
l2.add_at_tail(7)

print(add_2_numbers(l1.head, l2.head))


"""
Create a Doubly Linked List class. Write Instance Methods for this class to be able to
1. Remove a node when the node to be removed is given as input
2. Insert a node before a particluar node (both the node to be inserted and the node 
    before which the insertion is to happen will be given as input). If the node to be
    inserted  is
    - part of the linked list then shift its place to the dsired location
    - a new node, then insert the new node at the place desired.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def link_nodes(node1, node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node):
        # remove from head or tail
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev 
        
        # remove from inside the list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # remove the existing pointers on the node
        node.next = None
        node.prev = None
    
    def insert_before(self, node_position, node_insert):
        # check if the DLL has only one node
        if self.head == node_insert and self.tail == node_insert:
            return
        self.remove(node_insert) #if node to insert is part of the DLL
        node_insert.prev = node_position.prev
        node_insert.next = node_position

        #check if nodeposition is the head, point the head to node_to_insert
        if node_position == self.head:
            self.head = node_insert
        else:
            node_position.prev.next = node_insert
        node_position.prev = node_insert

    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.value, end=" "),;    
            current = current.next;   

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

linked_list_doubly = DoublyLinkedList()

link_nodes(one,two)
link_nodes(two,three)
link_nodes(three,four)
link_nodes(four,five)
linked_list_doubly.head = one
linked_list_doubly.tail = five

linked_list_doubly.display()
linked_list_doubly.insert_before(three, Node(6))
linked_list_doubly.display()