"""
Create a dictionary from the following pairs (key, value):
    'USA': 'Washington' 
    'Germany': 'Berlin' 
    'Austria': 'Vienna'
and print to the console
"""

from ast import Delete


dict = {'USA': 'Washington', 'Germany': 'Berlin', 'Austria': 'Vienna'}
print(dict)


"""
The following dictionary is given:

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

Use the appropriate method to extract all keys from the capitals

Expected result:
    dict_keys(['USA', 'Germany', 'Austria'])
"""

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
dict_keys = capitals.keys()
print(dict_keys)


"""
The following dictonary is given:

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
Using appropriate method, extract the list containing tuple 
objects(key,value) from the capitoals dictionary and print to console

Expected result:
    dict_items([('USA', 'Washington'), ('Germany', 'Berlin'), ('Austria', 'Vienna')])
"""

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.items())

"""
Using the dict.get() method, extract the value for the key 'Austria'
and print it to the console
"""
print(capitals.get('Austria'))


"""
The following dictionary is given:

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
Extract the value for the key 'APPL.US' and print to the console

Expected result:
    {'Apple Inc': 310}
"""
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks['AAPL.US'])


"""
Get the price for Microsoft (value for the 'Microsoft Corp' key) and
print to the console

Expected result:
    184
"""

print(stocks['MSFT.US']['Microsoft Corp'])

"""
Update the price for Microsoft to 190 and print the value for the 'MSFT.US'
key to the console

Expected result:
    {'Microsoft Corp': 190}
"""
stocks['MSFT.US']['Microsoft Corp'] = 190
print(stocks['MSFT.US'])


"""
The following dictionary is given:

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
Add a fourth pair to the dictionary with the key 'V.US' and the value
{'Visa Inc': 185} Print the value to console

Expected result:
dict_values([{'Microsoft Corp': 184}, {'Apple Inc': 310}, {'3M Co': 148}, {'Visa Inc': 185}])
"""
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks['V.US'] = {'Visa Inc': 185}
print(stocks.values())


"""
A list of tickers from the Dow Jones index is given:

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]
Transform the list into a list of a two-element tuple objects (index, ticker)
and print to the console.

Expected result:
(0, 'AAPL.US'), (1, 'AXP.US'), (2, 'BA.US'), (3, 'CAT.US'), (4, 'CSCO.US'), (5, 'CVX.US'), (6, 'DIS.US'), (7, 'DOW.US'), (8, 'GS.US'), (9, 'HD.US'), (10, 'IBM.US'), (11, 'INTC.US')]
"""

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

print(list(enumerate(tickers)))


"""
Transform the tickers into a dictionary and print to the console
"""
# list_tuple = list(enumerate(tickers))
# print(f' To tuple {list_tuple}')
# print(dict(enumerate(tickers)))
# dct = dict((y, x) for x, y in list_tuple)


"""
The following dictionary is given:

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
Extract a list of unique values (sorted alphabetically) from the 
project_ids dictionary and print to the console

Expected result:
    ['completed', 'in progress', 'open']
"""

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
result = list(set(project_ids.values()))
result.sort()
print(result)


# Delete (del)
"""
The following dictionary is given:
    stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
Delete the 'traffic' key pair from the dictionary and print to the console

"""

stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
del stats['traffic']
print(stats)


