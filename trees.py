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
    

    def find(self, value):
        if not self.root:
            return False
        tree = self.root 
        while tree:
            if value < tree.value:
                # move left
                tree = tree.left
            elif value > tree.value:
                # move right
                tree = tree.right 
            elif value == tree.value:
                return tree 
        return False
    

    def remove(self, value, current=self.root, parent=None):
        if not self.root:
            return False
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # found the node to be deleted
                # if node to be deleted has 2 children
                if current.left != None and current.right != None:
                    current.value = self.getMin(current.right)
                    self.remove(current.value, current.right, current)  #remove the min value
                elif parent != None:  # if deleting the root node
                    if current.left != None:  #if it has a lefft child. The right child has been taken care of above
                        current.value = current.lefft.value
                        current.left = current.left.left
                        current.right = current.left.right

    def getMin(self, node):
        while node.left != None:
            node = node.left
        return node.value


    

