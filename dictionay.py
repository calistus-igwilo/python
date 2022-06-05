"""
Create a dictionary from the following pairs (key, value):
    'USA': 'Washington' 
    'Germany': 'Berlin' 
    'Austria': 'Vienna'
and print to the console
"""

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


