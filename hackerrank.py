"""
Leap Year: A year is a leap year if:
    1. The year is a multiple of 400
    2. The year is a multiple of 4 but not a multiple of 100 
"""
import numbers
from turtle import position
from typing import Counter, Dict


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    return leap

"""
Given the participants' score sheet for your University Sports Day, you are required 
to find the runner-up score. You are given  scores. Store them in a list and find the 
score of the runner-up.
"""
numbers = [2, 3, 6, 6, 5]
numbers = Counter(numbers)
numbers = sorted(numbers.keys())
print(numbers[-2])

# Or
scores = [2, 3, 6, 6, 5]
result = list(set(scores))
result = sorted(result)
print(f' Second runner up {result[-2]}')


"""
Given the names and grades for each student in a class of students, store them in a 
nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names 
alphabetically and print each name on a new line
"""
record =[["chi", 20.0], ["beta", 50.0], ["alpha", 50.0], ["ojiugo", 30], ["madala", 30]]

# find the second position
scores = sorted(list(set([score[1] for score in record])))
position = scores[1]

# sort the list of second positions
sec_pos = sorted([item for item in record if item[1] == position])
for item in sec_pos:
    print(item[0])


"""
The provided code stub will read in a dictionary containing key/value pairs of 
name:[marks] for a list of students. Print the average of the marks array for the 
student name provided, showing 2 places after the decimal.
"""

student_marks = {'ojiugo': [20,30,40], 'uliaku': [30,50,70]}
query_name = 'uliaku'

data = [score[1] for score in student_marks.items() if query_name == score[0]]
result = float(sum(data[0])/len(data[0]))
print(f'{result} :2f')

"""
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555

Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
Note: Don't use anything related to strings
"""
for i in range(1, 5):
    print(i * 10**i // 9) # use math operation to get all 1s and multiply by index


"""
You are given a string S 
Your task is to print all possible permutations of size  of the string 
in lexicographic sorted order.
"""
from itertools import permutations
s, num = input().split()
result = sorted(list(permutations(s, int(num))))
for i in result:
    print("".join(i))


# """
# Read input from STDIN and display the cartesan space.

# Example 
# input 1: 1 2
# input 2: 3 4
# Output:  
#     (1, 3) (1, 4) (2, 3) (2, 4)
# """
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# result = [(i, j) for i in a for j in b]
# for i in result:
#     print(i, end=" ")

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
