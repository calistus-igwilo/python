"""
The gaming.txt file is attached to this excercise. This file has been loaded into 
the text variable. From the text list, delete all newline characters. Then delete
emply lines and print the text to the console.

text before: 

['Activision Blizzard\n', 
'\n', 
'Activision Blizzard, Inc. is a developer and publisher of interactive entertainment content and services. The Company develops and distributes content and services across various gaming platforms,\n', 
'including video game consoles, personal computers (PC) and mobile devices. Its segments include Activision Publishing, Inc. (Activision), Blizzard Entertainment, Inc. (Blizzard),\n', 
'King Digital Entertainment (King) and Other. Activision is a developer and publisher of interactive software products and content. Blizzard is engaged in developing and publishing of interactive\n', 
'software products and entertainment content, particularly in PC gaming. King is a mobile entertainment company. It is engaged in other businesses, including The Major League Gaming (MLG) business;\n', 
'The Activision Blizzard Studios (Studios) business, and The Activision Blizzard Distribution (Distribution) business. It also develops products spanning other genres, including action/adventure,\n', 
'role-playing and simulation.']

"""
from lib2to3.pgen2 import token


with open('gaming.txt', 'r') as file:
    text = file.readlines()
text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line)>0]
print(text)


"""
The list of product prices is given:
    net_price = [5.5, 4.0, 9.0, 10.0]
The VAT for these products is equal to 23%
    tax = 0.23
Using the list comprehension, calculate the gross price for each product. Round the 
price to two decimal places and print result to console.
"""
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]
gross_price = [round(num*(1+0.23),2) for num in net_price]
print(gross_price)


"""
The present value - pv and the investment value - n are given below:
    pv = 1000
    n = 10
Depending on the interest rates given below, calculate the future value fv of your
investment
    rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
round the result to full cent and print the result to the console

Expected result:
    [1104.62, 1218.99, 1343.92, 1480.24, 1628.89, 1790.85, 1967.15]
"""
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

fv = [round(pv*(1 + r)**n, 2) for r in rate]
print(fv)


"""
The present value - pv and the investment period - n are given below:
    pv = 1000
    n = 10
Depending on the interest rates given below, calculate the value of interest on 
investments:
    rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
Round the result to the full cent and print the result to the console.

Expected result:
    [104.62, 218.99, 343.92, 480.24, 628.89, 790.85, 967.15]
"""
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
fvs = [round(pv*(1 + r)**n, 2) for r in rate]
interest = [round(fv - pv, 2) for fv in fvs]
print(interest)


"""
The contents of the file plw.txt were loaded as follows:
    with open('plw.txt', 'r') as file:
        lines = file.read().splitlines()

lines variable:

['PLAYWAY', 
'', 
'PlayWay is a producer and publisher of computer and mobile games. The company is characterized by a very large number of development teams and a large number of games produced simultaneously.', 
"PlayWay sells, among others via the STEAM portal, AppStore and GooglePlay. The US and German markets are the two largest markets for the Group's sales.", 
'In addition, the company has PlayWay Campus - a campus for cooperating development teams.']

Task to perform:
1. Get rid of blank lines
2. Split each line into tokens/words as hsown below

Formatted result:

"""
with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()

lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]
print(lines)


"""
The contents of the file plw.txt were loaded as follows:
    with open('plw.txt', 'r') as file:
        lines = file.read()

lines variable:

Tasks to perform:
1. Change uppercase letters to lowercase
2. Remove commas and periods
3. Split the text into tokens 
4. Extract words with minimum of 8 characters length
5. Sort the words alphabetically
"""

with open('plw.txt', 'r') as file:
    lines = file.read()
lines = lines.lower()
lines = lines.replace(',','').replace('.','')
tokens = lines.split()
tokens = [token for token in tokens if len(token) >= 8]
tokens = sorted(tokens)
print(tokens)


"""
The following dictionary is given:
    data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
Convert the dictionary into the following list and print the result to console

Expected result:
    [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6]]
"""
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'),(1, 2, 3, 4, 5, 6)))
data = [[key, val] for key, val in data.items()]
print(data)

