"""
You are given an array of integers and another integer targetvalue. Write a function
that will take these inputs and return the indices of the 2 integers in the array
that add up targetvalue
"""
def target_value(arr, t):
    if arr == [] or len(arr) == 1:
        return arr
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if i + j == t:
                return arr[i], arr[j]
    return arr

arr = [2, 7, 3, -1, 4]
print(target_value(arr, 2))
        
