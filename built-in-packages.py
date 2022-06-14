"""
Print the calendar for 2020 to the console using the calendar built-in module

Expected result:

                                  2020

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                         1
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                    30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
27 28 29 30               25 26 27 28 29 30 31      29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2          1  2  3  4  5  6
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                          31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1          1  2  3  4  5  6
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
"""
import calendar
from datetime import datetime
print(calendar.calendar(2020))


"""
Using the datetime built-in module, calculate the difference for dates (date 2 - date 1)

date 1: 2020-06-01
date 2: 2020-07-18
"""
from datetime import date
date1 = date(2020,6,1)
date2 = date(2020,7,18)
diff = date2 - date1
print(diff)


"""
Using the built-module for regular expressions, find all digits in the following list:
    string = 'Python 3.8'
Print result to the console
Tip: Use the findall() function and the regular expression '\d'

Expected reault:
    ['3', '8']
"""
import re

string = 'Python 3.8'
#result = re.findall(r"/d", string)
result = re.findall(pattern=r"\d", string=string)
print(result)


"""
Using the built=in module for regular expressions, find all alphanumeric characters
in the following text
    string = '!@#$%^&45wc'
Print the result to the console.

Tip: Use the findall() function and the regular expression '\w'

Expected result:
    ['4', '5', 'w', 'c']
"""
string = '!@#$%^&45wc'
result = re.findall(pattern=r"\w", string=string)
print(result)


"""
Use the built-in module for the regular expressions, find all email addresses in 
the following text:
    raw_text = "Send an email to info@template.com or sales-info@template.it"
Print the result to the console

Tip: Use the findall() function and the regular expression '[\w\.-]+@[\w\.-]+'

Expected result:

"""
raw_text = "Send an email to info@template.com or sales-info@template.it"
result = re.findall(pattern=r'[\w\.-]+@[\w\.-]+', string=raw_text)
print(result)


"""
Using the built-in module for regular expressions, split the following text by 
whitespace (spaces):
    text = 'Programming in Python - from A to Z'
Print the result to the console

Tip: Use the re.split() function and the regular expression '\s+'
"""
text = 'Programming in Python - from A to Z'
result = re.split(pattern=r'\s+', string=text)
print(result)


"""
Using the string built-in module, print a string of lowercase and uppercase letters
to the console
"""
import string
 
print(string.ascii_letters)


"""
Using the collections built-in package, create a Counter class object that counts the
frequency of items in the following list:
    items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
"""
from collections import Counter
counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)


"""
Using the random built-in module set the random seed as follows:
    random.seed(12)
And select randomly [pseudo-random] an item from the list below
    items = ['python', 'java', 'sql', 'c++', 'c']
"""
import random

random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']
choice = random.choice(items)
print(choice)


"""
Using the random built-in module set the random seed as follows:
    random.seed(15)
And shuffle (pseudo-randomly) items in the follwing list;
    items = ['python', 'java', 'sql', 'c++', 'c']
In response, print the list to the console 
"""
random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']
random.shuffle(items)
print(items)


"""
Using the pickle built-in module, save the follwoing list tothe data.pickle file.
    ids = ['001', '003', '011']
"""
import pickle

ids = ['001', '003', '011']
with open('data.pickle', 'wb') as file:
    pickle.dump(ids, file)


"""
Using the json package, dump the follwoing dictionary:
    stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
to the string, sorted by keys with indent 4. Print the result to the console
"""
import json

stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}
result = json.dumps(stocks, sort_keys=True, indent=4)
print(result)
