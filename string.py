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


# Compress the string
"""
You are given a string S Suppose a character 'c' occurs consecutively X 
times in the string. Replace these consecutive occurrences of the 
character 'c' with (X, c) in the string.
"""
S = 1222311
def compress_string(S):
    result = []
    temp = []
    pointer = 1
    i = 0
    j = i+1
    cnt = 1


    if len(S) == 0:
        return "string must contain at least 1 element"
    while S(j):
        temp.append(S[i])
        while S[i] == S[j]:
            cnt += 1
            i += 1
        result.append((cnt, temp[-1]))
        temp = []
    print(result)


"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .
"""
def minion_game(string_):
    vowel_strings = 0
    consonant_strings = 0
    string_length = len(string_) # length of string

    for i in range(string_length):
        if string_[i] in "AEIOU":
            vowel_strings += string_length - i  # the number of substrings that can be formed from the length
        else:
            consonant_strings += string_length -i # the number of substrings that can be formed

    # Determine the winner
    if consonant_strings > vowel_strings:
        print("Stuart", consonant_strings )
    elif consonant_strings < vowel_strings:
        print("Kevin", vowel_strings)
    else:
        print("Draw")

minion_game("BANANA")


def merge_the_tools(string, k):
    sub_sequences = []
    temp = ""
    for i in range(0, len(string), k):
        sub_sequences.append((string[i:i+k]))
    print(sub_sequences)
    print("lenght of subsequence: ",len(sub_sequences))

    # check for duplicate alphabets
    for string in sub_sequences:
        for i in range(k):
            if string[i] not in temp:
                temp += string[i]
        print(temp)
        temp = ""

s = 'AAABCADDE'
merge_the_tools(s)


"""
You are given a string and your task is to swap cases. In other words, convert all 
lowercase letters to uppercase letters and vice versa.
"""
def swap_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].isupper():
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result

t = "Www.HackerRank.com"
swap_case(t)


"""
A user enters a string and a substring. You have to print the number of times that the 
substring occurs in the given string. String traversal will take place from left to right, 
not from right to left.
String letters are case-sensitive.
"""
def count_substring(string, sub_string):
    substring_length = len(sub_string)
    string_length = len(string)
    end = string_length - 2
    cnt = 0
    
    for i in range(0, end):
        if string[i:i+substring_length] == sub_string:
            cnt += 1
    return cnt 

s = "ABCDCDC"
sub = "CDC"
count_substring(s, sub)  # 2


"""
You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.

Output Format:
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
s = "qA2"
print(s.isalnum())
def string_type(s):
    temp = []
    
    for char in s:
        temp.append(char.isalnum())
    if True in temp:
        print(True)
    else:
        print(False)
    temp =[]

    for char in s:
        temp.append(char.isalpha())
    if True in temp:
        print(True)
    else:
        print(False)
    temp =[]

    for char in s:
        temp.append(char.isdigit())
    if True in temp:
        print(True)
    else:
        print(False)
    temp =[]

    for char in s:
        temp.append(char.islower())
    if True in temp:
        print(True)
    else:
        print(False)
    temp =[]

    for char in s:
        temp.append(char.isupper())
    if True in temp:
        print(True)
    else:
        print(False)
    temp =[]

z = "qA2"
string_type(z)        





                

