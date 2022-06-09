################################
# LAMBDA EXPRESSIONS
###############################
"""
The following list of words is given:
    stocks = ['playway', 'boombit', 'cd projekt']
Using the map() function and the lambda expression, transform the given
list into a list containing the lenghs of each word and print to console
"""
stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(lambda item: len(item), stocks))
print(length)


"""
Implement the sort_list() function that suorts a list of two-element
tupple objects according to the second element of the tuple

Tip: use sorted function

Example: 
Given: [(1, 3), (4, 1), (4, 2), (0, 7)]
Result: [(4, 1), (4, 2), (1, 3), (0, 7)]
"""
def sort_list(items):
    return sorted(items, key=lambda x: x[1])
print(sort_list([(1, 3), (4, 1), (4, 2), (0, 7)]))


"""
The func_1() function is defined below:
    def func_1(x, y):
        return x + y + 2
Using the lambda expression, define an analogous function and assign
it to the variable func_2
"""
func_2 = lambda x,y: x+y+2


"""
The following list is given
    items = [(3, 4), (2, 5), (1, 4), (6, 1)]
Sort the list by growing sum of squares of numbers in each tuple.
Use the sort() method and the lambda expression and print sorted
list to the console

Expected result
    [(1, 4), (3, 4), (2, 5), (6, 1)]
"""
items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda x: x[0]**2 + x[1]**2)
print(items)


"""
Sort the given list of dictionaries by price key 

stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]
Print sorted list to the console

Formated result:
[{'index': 'sWIG80', 'name': 'BBT', 'price': 22}, 
{'index': 'mWIG40', 'name': 'TEN', 'price': 304}, 
{'index': 'mWIG40', 'name': 'PLW', 'price': 309}]  
"""
stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]
result = sorted(stocks, key=lambda item: item['price'])
print(result)

"""
Extract companies from the 'mWIG40' index and print the result to 
the console

Formated result:

[{'index': 'mWIG40', 'name': 'TEN', 'price': 304}, 
{'index': 'mWIG40', 'name': 'PLW', 'price': 309}]
"""
result = list(filter(lambda item: item['index'] == 'mWIG40', stocks))
print(result)


"""
Convert the stocks list to a list of boolean values (True, False). True
if the company belongs to the 'mWIG40' index, False on the contrary and
print the result to the console

Tip: Use the map() function.

Expected result
    [True, True, False]
"""
result = list(map(lambda item: item['index'] == 'mWIG40', stocks))
print(result)


"""
The following list is given:
    items = ['P-1', 'R-2', 'D-4', 'F-6']
Using the map() function and the lambda expression, get rid of the '-'
(dash) from each element and print items list to the console.

Expected result:
    ['P1', 'R2', 'D4', 'F6']
"""
items = ['P-1', 'R-2', 'D-4', 'F-6']
result = list(map(lambda x: x.replace('-', ''), items))
print(result)


"""
Two lists are given:
    num1 = [4, 2, 6, 2, 11]
    num2 = [5, 2, 3, 3, 9]
Using the map() function and lambda expression, create a list containing
the remainders of dividing the first list by the second

Expected result:
    [4, 0, 0, 2, 2]
"""
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

result = list(map(lambda x, y: x % y, num1, num2 ))
print(result)

