"""
Design a Binary Search Tree class that supports the following:
1. Insert a value
2. Remove a value. This method shold remove the first occurence of a value
3. Find a value. If the value is found it should return the node with the value
    else return false.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
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
    

    def remove(self, value, current, parent=None):
        current = self.root
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
                    if current.left != None:  #if it has a lefft child only.
                        current.value = current.left.value
                        current.left = current.left.left
                        current.right = current.left.right
                    elif current.right != None:  # if it has a right child only
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        # this is a single node bst
                        self.root = None
                elif current == parent.left:
                    parent.left = current.left if current.left != None else current.right
                elif current == parent.right:
                    parent.right = current.left if current.left != None else current.right
                # break out of the while loop
                break
        return self

    def getMin(self, value):
        node = Node(value)
        while node.left != None:
            node = node.left
        return node.value

    def breadth_first(self):
        if self.root == None:
            return []
        arr = []
        # queue as array to save time (queue as linked list is better)
        queue = []
        node = self.root
        while len(queue):
            node = queue.pop(0)
            arr.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return arr 

    def dfs_pre_order(self):
        if self.root == None:
            return []
        arr = []
        current = self.root
        def trav(self, node):
            node = Node(self, node)
            arr.append(node)
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)
        trav(current)
        return arr


"""
Write a 4 instance methods for a Binary Search Tree class to traverse the BST
1. Method 1: traverse the tree breadth first and return an array that contains
all values of the BST
2. Method 2: traverse the tree depth first - in-order and return an array that 
contains all the values of the BST
3. Method 3: traverse the tree depth first - Pre-order and return an array that 
contains all the values fo the BST
4. Method 4: traverse the tree depth first - Post-order and return an array that
contains all the values of the BST
"""
# implemented in the BinarySearchTree class
# 1. breadth_first()



bst = BinarySearchTree()

bst.insert(20)
bst.insert(6)
bst.insert(35)
bst.insert(3)
bst.insert(8)
bst.insert(27)
bst.insert(55)
bst.insert(1)
bst.insert(3)
bst.insert(25)
bst.insert(29)
bst.insert(60)

print(f'breadth first: {bst.breadth_first()}')
