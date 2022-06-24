"""
You are given an array of integers and another integer targetvalue. Write a function
that will take these inputs and return the indices of the 2 integers in the array
that add up targetvalue
"""
# Method 1: Brute force
def target_value(arr, target):
    if arr == [] or len(arr) == 1:
        return []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return []
    # Time complexity = O(n**2). Space complexity = O(1)

arr = [2, 7, 3, -2, 4]
target = 2
print(f'Brute force solution: {target_value(arr, target)}')

# Method 2: Hash Table
def target_value_hash(arr, target):
    hashTable = {}
    for i in range(len(arr)):
        needed_value = target - arr[i]
        if needed_value in hashTable:
            return [i, hashTable[needed_value]]
        else:
            hashTable[arr[i]] = i
    return []
    # Time complexity = O(n). Space complexity = O(n)
print(f'hash table soluition: {target_value_hash(arr, target)}')     


"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t
are isomorphic if the characters in s can be replaced to get t. All occurrences of
hcaracter must be replaced with another character while preserving the order of 
characters. No two characters may map to the same character, but a character may 
map to itself. s and t consist of any valid ascii character
"""
def check_isomorphic(s, t):
    if len(s) != len(t):
        return False
    sHash = {}
    tHash = {}

    for i in range(len(s)-1):
        charS = s[i]
        charT = t[i]
        if charS not in sHash:
            sHash[charS] = charT
        if charT not in tHash:
            tHash[charT] = charS
        if sHash[charS] != charT or tHash[charT] != charS:
            return False
    return True
    # Time complexity = O(n). space complexity = O(1) since it uses ascii characters
    # which has a fixed size (max of 256)

s = "green"
t = "abccd"
print(check_isomorphic(t, s))