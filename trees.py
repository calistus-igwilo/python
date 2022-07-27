"""
Design a Binary Search Tree class that supports the following:
1. Insert a value
2. Remove a value. This method shold remove the first occurence of a value
3. Find a value. If the value is found it should return the node with the value
    else return false.
"""
from turtle import left


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node()
        if not self.root:  #if there is no root, make the node the root
            self.root = node 
            return self
        tree = self.root    # else, store the root in tree variable
        while True:
            if value < tree.value:
                # move left
                if not tree.left:  # if the node is a leaf
                    tree.left = node
                    return self 
                tree = tree.left
            else:
                # move right
                # value > = tree.value
                if not tree.right:
                    tree.right = node
                    return self 
                tree = tree.right 

    

