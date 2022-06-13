"""
Using dict comprehension, create a dictionary that maps the numbers 1 to 7 into squares
and print the result to the console

Expeted result:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
"""
from pickle import NONE


result = {num:num**2 for num in range(1, 8)}
print(result)


"""
The following list is given:
    stocks = ['Playway', 'CD Projekt', 'Boombit']
Use dict comprehension to build a dictionary that maps company names to the number of 
characters of its name and print the result to the console. 
    stocks = ['Playway', 'CD Projekt', 'Boombit']

Expected result:
    'Playway': 7, 'CD Projekt': 10, 'Boombit': 7}
"""
stocks = ['Playway', 'CD Projekt', 'Boombit']
result = {name:len(name) for name in stocks}
print(result)


"""
The following dictionary is given:
    stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
Use dict comprehension to replace values with keys and print the result to console

Expected result:
    {'001': 'Boombit', '002': 'CD Projekt', '003': 'Playway'}
"""
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result = {value:key for key, value in stocks.items()}
print(result)


"""
The following dictionary is given:
    stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
using dict comprehension extract a key:value pair from the dictionary with a value
greater than 100 and print the result to the console

Expected result:
    {'CD Projekt': 295, 'Playway': 350}
"""
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
result = {key:value for key, value in stocks.items() if value > 100}
print(result)


"""
Create a list consisting of dictionaries mapping consecutive digits from 1 to 9 
inclusive to their respective k-th powers, for k = 1,2,3

Print result to the console as shown below

Formated output:
[{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}, 
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}]
"""
result = [{i:i**j for i in range(1,10)} for j in range(1, 4)]
print(result)


"""
The following list of indexes is given:   
    indeks = ['WIG20', 'mWIG40', 'sWIG80']
and a list of properties for each index:
    properties = ['number of companies', 'companies', 'cap']
Use dict comprehension to create the follwoing dictionary:

{'WIG20': {'number of companies': None, 'companies': None, 'cap': None}, 
'mWIG40': {'number of companies': None, 'companies': None, 'cap': None}, 
'sWIG80': {'number of companies': None, 'companies': None, 'cap': None}}

Set the default value in each property to None and print the result to console.
"""
properties = ['number of companies', 'companies', 'cap']
indeks = ['WIG20', 'mWIG40', 'sWIG80']

result = {ind: {prop: None for prop in properties} for ind in indeks}
print(result)


"""
The following is given:
    indexes = ['WIG20', 'mWIG40', 'sWIG80']
Using dict comprehension, convert the above list into the following dictionary:
    {0: 'WIG20', 1: 'mWIG40', 2: 'sWIG80'}
Print resutl to console
"""
indexes = ['WIG20', 'mWIG40', 'sWIG80']
result = {key: val for key, val in enumerate(indexes) }
print(result)
