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
    
    def dfs_in_order(self):
        if self.root == None:
            return []
        arr = []
        current = self.root
        def trav(self, node):
            if node.left:
                trav(node.left)
            arr.append(node)
            if node.right:
                trav(node.right)
        trav(current)
        return arr

    # current, left, right
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

    # left, right, current
    def dfs_post_order(self):
        if self.root == None:
            return []
        arr = []
        current = self.root
        def trav(node):
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)
            arr.append(node)
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
# 2. dfs_in_order()
# 3. dfs_pre_order()
# 4. dfs_post_order()



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


"""
Write a function that takes the root of a binary tree, and returns the level order
traversal of its nodes' values. (i.e., from left to right, level by level). Initially
write an instance method for the Binary Search tree class to insert the values given 
as an array into the Binary tree (from left to right, level by level). Each value in 
the array which is not null is to be made a node and added to the tree
"""
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, arr):
        if len(arr) == 0:
            return
        i = 0
        # if root is null
        if not self.root:
            if arr[0] == None:
                return 
            else:
                node = Node(arr[0])
                self.root = node
                i += 1
                if i == len(arr):
                    return self
        # insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            # left
            if not current.left:
                if arr[i] is not None:
                    node = Node(arr[i])
                    current.left = node
                i += 1
                if i == len(arr):
                    return self
            if current.left:
                queue.append(current.left)
            # right
            if not current.right:
                if arr[i] is not None:
                    node = Node(arr[i])
                    current.right = node
                i += 1
                if i == len(arr):
                    return self
            if current.right:
                queue.append(current.right)


def level_order_traversal(root):
    if not root:
        return []
    output = []
    queue = [root]
    while len(queue):
        length = len(queue)
        count = 0
        curr_level_values = []
        while count < length:
            curr = queue.pop(0)
            curr_level_values.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
        output.append(curr_level_values)



tree = BinaryTree()
tree.insert([7,11,1,None,7,2,8,None,None,None,3,None,None,5,None])

print(level_order_traversal(tree.root))


"""
1. Given the root of a binary tree, imagine yourself standing on the right side of it
return the values of the nodes you can see ordered from top to bottom.
2. Given the root of the binary tree, imagine yourself standing on the left side of it
return the values of the nodes you can see ordered from top to bottom
"""
def right_view(root):
    if not root:
        return []
    right = []
    queue = [root]
    while len(queue):
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == length:
                right.append(current)
            if current.left:
                queue.append(current.ledft)
            if current.right:
                queue.append(current.right)
    return right 


def left_view(root):
    if not root:
        return []
    left = []
    queue = [root]
    while len(queue):
        length = len(queue)
        count = 0
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == 1:
                left.append(current)
            if current.left:
                queue.append(current.ledft)
            if current.right:
                queue.append(current.right)
    return left 


"""
Given the root of a binary tree, invert the tree, and return its root.
(Invert means to swap every left node for its corresponding right node/get mirror image)
"""
def invert_iterative(root):
    if not root:
        return []
    queue = [root]
    while len(queue):
        current = queue.pop(0)
        # swap left and right
        temp = current.right
        current.right = current.left
        current.left = temp 
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root