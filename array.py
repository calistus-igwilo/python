"""
You are given an array of integers in which each subsequent 
value is not less than  previous value. Write a function that
takes this array as an input and returns a new array with the 
squares of each number sorted in ascending order
"""
def square_num(arr):
    result = [num**2 for num in arr]
    result.sort()
    return result 

print(square_num([-4, -2, 1, 3, 4]))