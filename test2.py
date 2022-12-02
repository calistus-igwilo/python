from curses.ascii import islower
from itertools import combinations, permutations



x = [1, 2, 3, 4]
y = [5, 6]
x.append(y)
print(x)


"""
Rotate an array to the right by k elements
"""
def rotate_array(arr, k):
    end = len(arr)-1
    if k <= 0:
        return arr
    for i in range(0, k, 1):
        #a, b = arr[0], arr[end]
        # arr = [arr[end]] + [arr[0]] + arr[1:end]
        arr = [arr[end]] + arr[0:end]
    return arr
print(rotate_array([1, 2, 3, 4, 5], 4))


text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

# words = text.lower().strip().replace('.', '').split()
# result = []
# for word in words:
#     if len(word) > 6:
#         result.append(word)
# print(result)

# Another solution using list comprehension
words = text.lower().strip().replace('.', '').replace(',', '').split()
words = [word for word in words if len(word) > 6]
print(words)


###############################
x=1; y=1; z=2; n=3
result = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c) != n]
print(result)

################################

def score_words(words):
    str = words.split()
    score = 0

    for word in str:
        if len(word)%2 == 0:
            score+=2
    print(score)

score_words("programming is awesome")
#################################

# All substrings of a string and calculate how many that starts with vowels and consonants
def minion_game(string_):
    vowel_strings = 0
    consonant_strings = 0
    string_length = len(string_) # length of string

    for i in range(string_length):
        if string_[i] in "AEIOU":
            vowel_strings += string_length - i
        else:
            consonant_strings += string_length -i 

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
merge_the_tools(s, 3)


def swap_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].isupper():
           s = s.replace(s[i], s[i].upper())
        else: 
            s = s.replace(s[i], s[i].lower())
        
            
    print(s)
    return s

t = "Www.HackerRank.com"
swap_case(t)

B = "baNM.y"
C = "caLY"
d = ""
if B[1].islower():
    d += B[1].upper()
print(d)
print(B[4].isupper())
print(B[1].upper())
print(C[2].isupper())
