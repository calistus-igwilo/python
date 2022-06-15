"""
Traverse list in parralel using the zip() function. Given:
    letters = ['a', 'b', 'c']
    numbers = [0, 1, 2]
Expected result:
    Letter: a
    Number: 0
    Letter: b
    Number: 1
    Letter: c
    Number: 2
"""
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')


"""
Use zip() to iterate through two dictionaries in parralel 

Expected result:
name -> John
name -> Jane
last_name -> Doe
last_name -> Doe
job -> Python Consultant
job -> Community Manager
"""
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)


"""
Separate a list tuples elements into independent sequences
    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

Expected result:
    numbers: (1, 2, 3, 4)
    letters: ('a', 'b', 'c', 'd')
"""
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(f'numbers: {numbers}')
print(f'letters: {letters}')


"""
Calculating in pairs using zip() function. Given the following monthly sales data:
    total_sales = [52000.00, 51000.00, 48000.00]
    prod_cost = [46800.00, 45900.00, 43200.00]
calculate the monthly profit

Expected result:
    Total profit: 5200.0 
    Total profit: 5100.0 
    Total profit: 4800.0 
"""
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]

for sales, cost in zip(total_sales, prod_cost):
    profit = sales - cost
    print(f'Total profit: {profit}')


"""
Build dictionary from two lists using the zip() function. Given the following:
    fields = ['name', 'last_name', 'age', 'job']
    values = ['John', 'Doe', '45', 'Python Developer']
Expected result:
    {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
"""
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(a_dict)