import array
from curses.ascii import isdigit


nums = [2,1,2,3,5]
missing = [num for num in range(1, len(nums)+1) if num not in nums]
duplicate = [num for num in nums if nums.count(num)>1]
result = (duplicate[1], missing[0])
print(result)

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# result = [(i, j) for i in a for j in b]
# for i in result:
#     print(i, end=" ")

# s, num = input().split()
# print(f's: {s}, num: {num}')

"""
Valid Parenthesis:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
def brackets(s):
    stack = []
    if len(s) % 2 != 0:
        return 'invalid'
    dic = {'(': ')', '{': '}', '[': ']' }
    for i in s:
        if i in dic.keys():
            stack.append(i)
            print(stack)
        else:
            if stack == []:
                return 'invalid'
            a = stack.pop()
            if i != dic[a]:
                return 'invalid'
    return 'valid'

s = "({[]})"
print(brackets(s))

# print(f's: {s}')

# stack2 = []
# if stack2:
#     print('Yes')
# else:
#     print("No")

arr = [2, 3]
print(f' Type arr: {type(arr)}')
if type(arr) == list:
    print(f'{arr} is a list array')
else:
    print("Not a list array")

# l = [1, 2, 3]
# permutation = [[i, j, k] for i, j, k in l]
# print(f'Permutation of {l}: {permutation}')

lines = [1,2,3,4,5,6,7,8,9]
print(lines[-4:])

# import re
# with open('log.txt', 'r') as lines:
#     for line in lines:
#         #print(line[3])
#         print(line.split("[")[1].split("]")[0])
#         #print(line.split()[3].strip("[]"))
#         #print(line.split("[" or "]"[3:5]))
#         #print(" ".join(line.split()[3:5]).strip("[]"))
#         #print(re.split("\[|\]", line)[1])


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
linked_list_doubly.remove(two)
linked_list_doubly.display()


height = 100
bounce = 1
while bounce <= 3:
    height = height * (3/5)
    bounce += 1
new = height
print(new)


S = "111222311"
def compress_string(S):
    result = []
    temp = []
    i = 0
    j = i+1
    cnt = 1

    if len(S) == 0:
        return "string must contain at least 1 element"
    while S[j]:
        temp.append(S[i])
        while S[i] == S[j]:
            cnt += 1
            i += 1
        result.append((cnt, temp[-1]))
        temp = []
    print(f'Groups: {result}')

compress_string(S)

arr = [1, 2, 3, 4]
print(f'Arr.pop {arr.pop([0])}')