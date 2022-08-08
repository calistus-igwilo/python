# # # Binary search tree
class binarySearchTree:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val):
        # check if there is no root
        if (self.val == None):
            self.val = val
        # check where to insert
        else:
            # check for duplicate then stop and return
            if val == self.val: return 'no duplicates aloowed in binary search tree'
            # check if value to be inserted < currentNode's value
            if (val < self.val):
                # check if there is a left node to currentNode if true then recurse
                if(self.left):
                    self.left.insert(val)
                # insert where left of currentNode when currentNode.left=None
                else: self.left = binarySearchTree(val)

            # same steps as above here the condition we check is value to be inserted > currentNode's value
            else:
                if(self.right):
                    self.right.insert(val)
                else: self.right = binarySearchTree(val)




    def breadthFirstSearch(self):
        currentNode = self
        bfs_list = []
        queue = []
        queue.insert(0,currentNode)
        while(len(queue) > 0):
            currentNode = queue.pop()
            bfs_list.append(currentNode.val)
            if(currentNode.left):
                queue.insert(0,currentNode.left)
            if(currentNode.right):
                queue.insert(0,currentNode.right)

        return bfs_list

    # In order means first left child, then parent, at last right child
    def depthFirstSearch_INorder(self):
        return self.traverseInOrder([])

    # Pre order means first parent, then left child, at last right child
    def depthFirstSearch_PREorder(self):
        return self.traversePreOrder([])

    # Post order means first left child, then right child , at last parent
    def depthFirstSearch_POSTorder(self):
        return self.traversePostOrder([])

    def traverseInOrder(self, lst):
        if (self.left):
            self.left.traverseInOrder(lst)
        lst.append(self.val)
        if (self.right):
            self.right.traverseInOrder(lst)
        return lst

    def traversePreOrder(self, lst):
        lst.append(self.val)
        if (self.left):
            self.left.traversePreOrder(lst)
        if (self.right):
            self.right.traversePreOrder(lst)
        return lst

    def traversePostOrder(self, lst):
        if (self.left):
            self.left.traversePostOrder(lst)
        if (self.right):
            self.right.traversePostOrder(lst)
        lst.append(self.val)
        return lst

    def findNodeAndItsParent(self,val, parent = None):
        # returning the node and its parent so we can delete the node and reconstruct the tree from its parent
        if val == self.val: return self, parent
        if (val < self.val):
            if (self.left):
                return self.left.findNodeAndItsParent(val, self)
            else: return 'Not found'
        else:
            if (self.right):
                return  self.right.findNodeAndItsParent(val, self)
            else: return 'Not found'

    # deleteing a node means we have to rearrange some part of the tree
    def delete(self,val):
        # check if the value we want to delete is in the tree
        if(self.findNodeAndItsParent(val)=='Not found'): return 'Node is not in tree'
        # we get the node we want to delete and its parent-node from findNodeAndItsParent method
        deleteing_node, parent_node = self.findNodeAndItsParent(val)
        # check how many children nodes does the node we are going to delete have by traversePreOrder from the deleteing_node
        nodes_effected = deleteing_node.traversePreOrder([])
        # if len(nodes_effected)==1 means, the node to be deleted doesn't have any children
        # so we can just check from its parent node the position(left or right) of node we want to delete
        # and point the position to 'None' i.e node is deleted
        if (len(nodes_effected)==1):
            if (parent_node.left.val == deleteing_node.val) : parent_node.left = None
            else: parent_node.right = None
            return 'Succesfully deleted'
        # if len(nodes_effected) > 1 which means the node we are going to delete has 'children',
        # so the tree must be rearranged from the deleteing_node
        else:
            # if the node we want to delete doesn't have any parent means the node to be deleted is 'root' node
            if (parent_node == None):
                nodes_effected.remove(deleteing_node.val)
                # make the 'root' nodee i.e self value,left,right to None,
                # this means we need to implement a new tree again without the delted node
                self.left = None
                self.right = None
                self.val = None
                # construction of new tree
                for node in nodes_effected:
                    self.insert(node)
                return 'Succesfully deleted'

            # if the node we want to delete has a parent
            # traverse from parent_node
            nodes_effected = parent_node.traversePreOrder([])
            # deleting the node
            if (parent_node.left == deleteing_node) : parent_node.left = None
            else: parent_node.right = None
            # removeing the parent_node, deleteing_node and inserting the nodes_effected in the tree
            nodes_effected.remove(deleteing_node.val)
            nodes_effected.remove(parent_node.val)
            for node in nodes_effected:
                self.insert(node)

        return 'Successfully deleted'


bst = binarySearchTree()
bst.insert(7)
bst.insert(4)
bst.insert(9)
bst.insert(0)
bst.insert(5)
bst.insert(8)
bst.insert(13)

#          7
#        /  \
#      /     \
#     4        9
#    / \      /  \
#   0   5    8    13


print('IN order: ',bst.depthFirstSearch_INorder()) # useful in sorting the tree in ascending order
print('PRE order:' ,bst.depthFirstSearch_PREorder()) # pre order is useful in reconstructing a tree
print('POST order:', bst.depthFirstSearch_POSTorder()) # useful in finding the leaf nodes

print(bst.delete(5))
print(bst.delete(9))
print(bst.delete(7))

# after deleting
print('IN order: ',bst.depthFirstSearch_INorder())




"""
Another Implementation
"""
class GFG :
	@staticmethod
	def main( args) :
		tree = BST()
		tree.insert(30)
		tree.insert(50)
		tree.insert(15)
		tree.insert(20)
		tree.insert(10)
		tree.insert(40)
		tree.insert(60)
		tree.inorder()
class Node :
	left = None
	val = 0
	right = None
	def __init__(self, val) :
		self.val = val
class BST :
	root = None
	def insert(self, key) :
		node = Node(key)
		if (self.root == None) :
			self.root = node
			return
		prev = None
		temp = self.root
		while (temp != None) :
			if (temp.val > key) :
				prev = temp
				temp = temp.left
			elif(temp.val < key) :
				prev = temp
				temp = temp.right
		if (prev.val > key) :
			prev.left = node
		else :
			prev.right = node
	def inorder(self) :
		temp = self.root
		stack = []
		while (temp != None or not (len(stack) == 0)) :
			if (temp != None) :
				stack.append(temp)
				temp = temp.left
			else :
				temp = stack.pop()
				print(str(temp.val) + " ", end ="")
				temp = temp.right
	
if __name__=="__main__":
	GFG.main([])
	
	# This code is contributed by rastogik346.
