"""
The list of companies from the WIG.GAMES index is given with the closing
price and currency:

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
Using the continue statement, create a for loop that will change the 
closing price from USD to PLN in the dictionary. Take USDPLN = 4.0

Expected result
{'11B': [362.5, 'PLN'], 'CDR': [297.0, 'PLN'], 'CIG': [0.85, 'PLN'], 'PLW': [318.0, 'PLN'], 'TEN': [300.0, 'PLN']}
"""
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] *= 4.0
    info[1] = 'PLN'
print(gaming)


"""
The list of names is given (one missing):
    names = ['Jack', 'Leon', 'Alice', None, 'Bob']
Using the continue statement, print only the correct names to the
console as shown below

Expected result:
    Jack
    Leon
    Alice
    Bob
"""
names = ['Jack', 'Leon', 'Alice', None, 'Bob']
for name in names:
    if name is None:
        continue
    print(name)