"""
You are given a string consisting of only lowercase and uppercase English Alphabets 
and integers 0 to 9. Write a function that will take this string as input and return 
the index of the first character that is repeating.
"""

from posixpath import split
from turtle import clear


def repeat(s):
    hashTable = {}
    for i in range(len(s)-1):
        if s[i] in hashTable:
            return i
        else:
            hashTable[s[i]] = i
    return []

s = "abcdeefgghhij"
print(repeat(s))

"""
You are given a string consisting of only lowercase and uppercase English Alphabets 
and integers 0 to 9. Write a function that will take this string as input and return 
the index of the first character that is non-repeating.
"""
# Method 1: 
def non_repeat(s):
    repeats = []
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            repeats.append(s[i])
    for i in range(len(s)):
        if s[i] not in repeats:
            return i
    return None
    # Time complexity = O(n). Space complexity = O(n)
s = "abaccbd"
print(non_repeat(s))

# Method 2: Improved brute force
def non_repeat(s):
    for i in range(len(s)):
        repeat = False
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                repeat = True
        if repeat == False:
            return i
    return None
    # Time complexity = O(n**2). Space complexity = O(1)
print(non_repeat(s))

# Method 3 Use of Hash Table
def non_repeat(s):
    hashTable = {}
    for i in s:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    for i in range(len(s)):
        if hashTable[s[i]] == 1:
            return i
    return None
    # Time complexity = O(n). 
    # Space complexity = O(1) because s has a fixed value (26 upper + 26 lower + 10 digits)
print(non_repeat(s))


"""
You are given a string. Write a function to check whether the string is a 
palindrome or not.
"""
def palindrome(s):
    str_ = ""
    for i in range(len(s)-1, -1, -1):
        str_ += s[i]
    print(str_)
    if str_ == s:
        return True
    return False
    # Time complexity = O(n**2) because strings are immutable, so append creates a
    # new string for each call.
    # Space complexity = O(n)
s = "abba"
print(palindrome(s))

# Method 2: Appending to an array
def palindrome(s):
    arr = []
    for i in range(len(s)-1, -1, -1):
        arr.append(s[i])
    result = ''.join(arr)
    if s == result:
        return True
    return False
    # Time complexity = O(n) because append to array is a constant time operation
    # and the array was traversed once.
    # Space complexity = O(n) as extra sapce was created to store the new array
print(palindrome(s))

# Method 3
def palindrome(s):
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    # Time complexity = O(n)
    # Space complexity = O(1) since no extra space was created
print(palindrome(s))


"""
Given a string s, find the length of the longest substring without repeating characters
"""
def max_substr(s):
    strList = []
    hashTable = {}
    max_ = 0
    start = 0
    for i in range(len(s)-1):
        if s[i] not in hashTable:
            hashTable[s[i]] = i
            max_ = max(start, i - start+1)
        else:
            strList.append(s[start:i])
            start = max(start, hashTable[s[i]]+1)
            hashTable[s[i]] = i
    print(f'Substrings: {strList}')
    return max_
    # Time complexity = O(n). Space complexity = O(n)
s = 'abcdbefghijklmef'
print(max_substr(s))          


"""
Given an array of strings consisting of lower case English letters, group the 
anagrams together. You can return the answer in any order. An Anagram is a 
word or phrase formed by rearranging the letters of a different word or phrase,
using all the original letters exactly once.
"""
def anagrams(arr):
    list_ = []
    hashTable = {}
    if len(arr) == 1 or len(arr) == 0:
        return arr
    print(arr)
    sortList = [''.join(sorted(item)) for item in arr]
    for i in range(len(arr)):
        if sortList[i] in hashTable:
            hashTable[sortList[i]] += [arr[i]]
        else: 
            hashTable[sortList[i]] =  [arr[i]]
    return hashTable.values()
    # Time complexity = O(S x nlogn) where S = number of strings and n = max number of
    # strings in the character.
    # Space complexity = O(S x n)

arr = ['arc', 'abc', 'car', 'cat', 'act', 'acb', 'atc']
print(anagrams(arr))


"""
Given an array of integers which is sorted in ascending order, and a target integer,
write a function to search for whether the target integer is there in the given array.
If it is there, then return its index. Otherwise, return -1. You must write an 
algorithm with O(logn) runtime complexity.
"""    
def binary_search(nums, target):
    pointerLeft = 0
    pointerRight = len(nums)-1
    while pointerLeft <= pointerRight:
        middle = (pointerRight + pointerLeft) // 2
        print(f'pointerLeft: {pointerLeft}, pointerRight: {pointerRight}')
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            pointerRight = middle - 1
        elif target > nums[middle]:
            pointerLeft = middle + 1        
    return -1
nums = [2, 3, 7, 9, 11, 23, 37, 81, 87, 89]
print(binary_search(nums, 9))


"""
You are given an integer array nums sorted in ascending order (with disctinct values). 
Prior to being passed to your function, nums is possibly rotated at an unkown pivot
index k (1 <= k < nums.lenght) such that the resulting array is 
[nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given an integer target, return the index of target if it is in the array, else return
-1. You must write an alogrithm with O(logn) runtime complexity.
"""
def search_rotation(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] < nums[middle]: 
            if nums[left] <= target and target < nums[middle]:
                right = middle-1
            else:
                left = middle+1
        else:
            if nums[middle] < target and target <= nums[right]:
                left = middle+1
            else:
                right = middle-1
    return -1
nums = [5,6,7,8,9,1,2,3,4]
target = 3
print(search_rotation(nums, target))








                

