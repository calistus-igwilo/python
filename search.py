"""
You are given an array of integers sorted in non-decreasing order, find the starting 
and ending position of a given target value. If target is not found in the array, 
return [-1, -1]. You must write an algorithm with O(logn) runtime complexity
"""
def start_end_sorted_array(nums, target):
    left_extreme = left_index(nums, target)
    right_extreme = right_index(nums, target)

    return [left_extreme, right_extreme]

def left_index(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            if middle == 0:
                return middle
            if nums[middle -1] == target:
                right = middle-1
            else:
                return middle
        else:
            if target < nums[middle]:
                right = middle -1
            else:
                left = middle + 1
    return -1

def right_index(nums,targe):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            if middle == len(nums)-1:
                return middle
            if nums[middle + 1] == target:
                left = middle+1
            else: 
                return middle
        else: 
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

nums = [1,2,3,3,3,3,4,5]
target = 3
print(start_end_sorted_array(nums, target))


"""
Search in Matrix: Write an efficient algorithm that searches for a value target in 
an m x n integer matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right
- The first integer of each row is greater than the last integer of the previous row
If the value is there in the matrix, retrun true, else false.
"""
def search_matrix(matrix, target):
    top = 0
    bottom = len(matrix)-1
    # Find the array that contains the target and store it in nums
    while top <= bottom:
        middle = (top + bottom) // 2
        if matrix[middle][0] <= target and matrix[middle][-1] >= target:
            nums = matrix[middle] 
        if matrix[middle][0] > target:
            bottom = middle - 1
        else:
            top = middle + 1

    # Use binary search to find the target in the array above
    left = 0
    right = len(nums)-1
    while left <= right:
        midpoint = (left + right) // 2
        if nums[midpoint] == target:
            return True
        if nums[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return False



matrix = [[1,5,7,11], [12,13,17,20], [25,26,30,31], [32,35,39,43], [45,60,62,65]]
target = 62
print(search_matrix(matrix, target))
