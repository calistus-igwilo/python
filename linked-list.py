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
