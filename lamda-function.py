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
