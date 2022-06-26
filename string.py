"""
You are given a string consisting of only lowercase and uppercase English Alphabets 
and integers 0 to 9. Write a function that will take this string as input and return 
the index of the first character that is repeating.
"""
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







                

