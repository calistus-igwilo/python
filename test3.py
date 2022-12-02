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
count_substring(s, sub)


def string_type(s):
    temp = []
    
    for char in s:
        temp.append(char.isalpha())
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
