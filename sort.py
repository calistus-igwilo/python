"""
Bubble Sort: You are given an array of integers. Write a function that will take
this array as input and return the sorted array using Bubble sort.
"""
def bubble_sort(nums):
    sorted_ = False # use this to know when there is no more swaps
    cnt = 0
    while sorted_ == False:
        sorted_ = True
        for i in range(len(nums)-1-cnt):  # cnt help to skip biggest nums that have been pushed to the end
            j = i+1
            if len(nums) == 0 or len(nums) == 1:
                return nums
            if nums[i] > nums[j]:
                a, b = nums[i], nums[j]
                nums[i], nums[j] = b, a
                sorted_ = False  # only false when items are swapped
        cnt += 1
    return nums
    # Time complexity = O(n**2). Space complexity = O(1)

nums = [2,3,7,1,8]
print(bubble_sort(nums))


"""
Given an array of integers. Write a function that will take this array as input
and return sorted array using insertion sort
"""
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i-1
        temp = nums[i]
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums

nums = [4,3,2,1]
print(insertion_sort(nums))


"""
You are given an array of integers. Write a function that will take this array as 
input and return the sorted array using Selection sort.
"""
def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i+1, len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j
        if i != smallest: 
            nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
nums = [4,3,2,1,2]
print(selection_sort(nums))


"""
Merge sort
"""
def merge_sorted_array(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])  #push the remaining arr1 elements into merged array
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])  # push the remaining arr2 elements into merged array
        j += 1
    return merged_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    leftside = merge_sort(arr[:middle])
    rightside = merge_sort(arr[middle:])
    return merge_sorted_array(leftside, rightside)

arr = [5,3,7,8,1,9,12]
print(merge_sort(arr))


"""
Quick Sort: You are given an array of integers. Write a function that will take this
array as input and return the sorted array using Quick sort
"""
