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

nums = [2,3,7,1,8]
print(bubble_sort(nums))

        

