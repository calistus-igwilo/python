"""
Design a Stack: 
Implement a Stack:
1. using an Array
2. with a Stack class using a Linked list
One should be able to add to the stack and remove from the stack following the LIFO
property.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Use a singly linked list to implement stack. 
    Add and remove nodes at the beginning to achieve O(1) time complexity
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add_at_beginning(self, value):
        node = Node(value)
        #check if SLL is empty, and make the node the head and tail
        if not self.first:
            self.first = node
            self.last = node
        else:
            # add node at the begining
            temp = self.first
            self.first = node
            self.first.next = temp
        self.size += 1
        return self
    
    def remove_from_begining(self):
        #check if stack is empty and return None
        if not self.first:
            return None
        temp = self.first  #to be able to return the removed node
        self.first = self.first.next
        self.size -= 1
        if self.size == 0: #if the last node was removed
            self.last = None
        return temp
    
    def display(self):    
        #Node current will point to head    
        current = self.first   
        if(self.first == None):    
            print("List is empty")   
            return;    
        print("Nodes of doubly linked list: ")   
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.value, end=" ")   
            current = current.next

stack = Stack()
stack.add_at_beginning(1)
stack.add_at_beginning(2)
stack.display()
stack.remove_from_begining()
stack.display()

        



