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
        print("Nodes of singly linked list: ")   
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


"""
Reverse polish notation:
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid 
operators are +, -, *, and / Note that division between two integers should truncate
toward zero. It is guaranteed that the given RPN expression is always valid. That 
means the expression would always evaluate to a result, and there will not be any
division by zero operation. The input is an array of strings where each element is
either a valid operator or an integer. E.g ["1", "2", "+"]
"""

class StackArray:
    """ LIFO Stack implementation using Python list/array as underlying storage"""
    def __init__(self):
        """ Create an empty stack """
        self._data = []   #non-public list instance

    def __len__(self):
        """ Return the number of elements in the stack """
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty"""
        return len(self._data) == 0

    def push(self, value):
        """Add value/element to the top of the stack"""
        self._data.append(value)

    def top(self):
        """Return (but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]  # last item in the list
    
    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()  # remove last item from the list
        




