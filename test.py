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
    print(f'{arr} is an array')
else:
    print("Not an array")