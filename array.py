"""
You are given an array of integers in which each subsequent 
value is not less than  previous value. Write a function that
takes this array as an input and returns a new array with the 
squares of each number sorted in ascending order
"""
from operator import truediv


def square_num(arr):
    result = [num**2 for num in arr]
    result.sort()
    return result 

print(square_num([-4, -2, 1, 3, 4]))

"""
An array is monotonic if it is either monotone increasing or monotone
decreasing. An array is monotone increasing if all its elements from left
to right are non-decreasing. An array is monotone decreasing if all its
elements from left to right are non-increasing. Given an integer array
return true if the given array is monotonic, or false otherwise.
"""
def monotonic(arr):
    end = len(arr) - 1
    if len(arr) == 0 or len(arr) == 1:
        return True 
    elif arr[0] > arr[end]:
        for i in range(end - 1):
            if arr[i] < arr[i+1]:
                return False
    elif arr[0] < arr[end]:
        for i in range(end-1):
            if arr[i] > arr[i+1]:
                return False
    elif arr[0] == arr[end]:
        for i in range(end-1):
            if i != i+1:
                return False
    
    return True
            
print(monotonic([-2, 3, 6, 8]))


"""
Rotate an array to the right by k elements
"""
def rotate_array(arr, k):
    end = len(arr)-1
    if k <= 0:
        return arr
    for i in range(0, k, 1):
        #a, b = arr[0], arr[end]
        arr = [arr[end]] + [arr[0]] + arr[1:end]
    return arr
print(rotate_array([1, 2, 3, 4], 4))


"""
You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the nth line are (i,0) and 
(i, height[i]). 
Find two lines that together with the x-axis form a container, such that 
the container contains the most water (depth is constant across containers)
Return the area (that the 2lines and the x axis make) of container which
can store the max amount of water. 
Notice that you may not slant the container.
"""
def max_area_brute(arr):
    end = len(arr)-2
    max_ = 0
    for i in range(end):
        for j in range(i+1, end+2):
            area = min(arr[i], arr[j]) * (j-i)
            if area > max_:
                max_ = area        
    return max_
# Note; the time complexity is O(n**2) since the array was traversed
# twice.  The space complexity is O(1) since no extra space was created
print(max_area_brute([9,1,2,3,10]))

def max_area_optimum(arr):
    end = len(arr)-1
    pointerLeft = 0
    pointerRight = end
    area = 0
    while pointerLeft < pointerRight:
        width = pointerRight - pointerLeft
        height = min(arr[pointerLeft], arr[pointerRight])
        newArea = width * height
        area = max(area, newArea)
        if arr[pointerLeft] < arr[pointerRight]:
            pointerLeft += 1
        else:
            pointerRight -= 1
    return area
# Note: Time complexity for this is O(n) since the array was traversed
# only once. Space complexity is O(1) since no extra space was created 
print(max_area_optimum([9,1,2,3,10]))


