##############################
# INBUILT FUNCTIONS
##############################
"""
The variable x
    x = -1.5
and the follwing expreasion are given:
    expression = 'x**2 + x'
Using the appropriate function, calculate thevalue of this expression 
and print the result to the console

Tip: Use the eval() funtion.
"""
x = -1.5
expression = 'x**2 + x'
print(eval(expression))


"""
The following variables are given:

var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

Using the appropriate function, chek if the variables are instances 
of tuple class. Print the result to the console

Tip: Use the isinstance() built-in function.
"""
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))


"""
The following list is given:
    characters = ['k', 'b', 'c', 'j', 'z', 'w']
Using the built-in functions, return the first and the last letter in 
alphabetical order from the list and print the result to the console

Tip: use the min() and max() functions.

Expected result
    First: b
    Last: z
"""
characters = ['k', 'b', 'c', 'j', 'z', 'w']
print((f'First: {min(characters)}'))
print((f'Last: {max(characters)}'))


"""
Two tuples are given:

    ticker = ('TEN', 'PLW', 'CDR')
    full_name = ('Ten Square Games', 'Playway', 'CD Projekt')
Using appropriate built-in function, create a list consisting of 
tuples (ticker, full_name) and print the result to the console

Tip: use the zip() function.

Expected result:
    [('TEN', 'Ten Square Games'), ('PLW', 'Playway'), ('CDR', 'CD Projekt')]
"""
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')
result = list(zip(ticker, full_name))
print(result)


"""
Using the appropriate built-in function, verify if all elements of the 
following tuple return a logical value True
    items = (' ', '0', 0.1, True)
Print the result to the console

Exptected result:
    True
"""
items = (' ', '0', 0.1, True)
print(all(items))


"""
Using the appropriate built-in function, verify if any element of the 
following tuple returns the boolean value True
    items = ('', 0.0, 0, False)
Print the result to the console
"""
items = ('', 0.0, 0, False)
print(all(items))


"""
Count the number of ones in the binary representaion of the number;
    number = 234
print the resutl to the console
"""
number = 234
binary = bin(number)
binary = binary[2:]  # as the first two digits are representations
print(binary.count('1'))

#################################
# DEFINING YOUR OWN FUNCTIONS
#################################

"""
Implement a function called maximum() that returns the maximum of two
numbers. Use conditional statement
"""
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print(maximum(2,6))


"""
Implement a function called maximum() that returns the maximum of three
numbers. Use conditional statement
"""
def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z
print(maximum(3,2,5))


"""
Implement a function called multi(), which accepts an iterable 
object (list, tuple) as an argument and returns the product of all
elements of this iterable object.
"""
def multi(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
print(multi([3, 2, 4]))


"""
Implement a function map_longest() that accepts the list of words and
reutn the word with the longest length in the list.
"""
def map_longest(words):
    dic = {word: len(word) for word in words}
    longest = max(dic, key= lambda x: dic[x])
    return longest

print(map_longest(['python', 'sql', 'javascript']))


"""
Implement a function called filter_ge_6() that takes a list of word 
and returns list of words with the length greater than or equal to 
6 characters

"""
def filter_ge_6(words):
    fil = [word for word in words if len(word)>=6]
    return fil

print(filter_ge_6(['python', 'sql', 'javascript']))


"""
Implement a function factorial() that calculates the factorial for a
given number.
"""
def factorial(num):
    #numbers = [n for n in range(1, num+1)]
    result = 1
    for n in range(1, num+1):
        result *=n 
    return result

print(factorial(10))


"""
Implement a function count_str(), which returns the number of str objects
in an iterable object (list tuple, set).
"""
def count_str(obj):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total


"""
Implement a function count_str(), which returns the number of str objects
with a lenght more than 2 characters from an iterable object (list tuple, set).
"""
def count_str(obj):
    total = 0
    for item in items:
        if isinstance(item, str):
            if len(item) > 2:
                total += 1
    return total


"""
Implement a function remove_duplicates() that removes duplicates from
the list (the order of the items in the list does not have to be kept)
"""
def remove_duplicates(string):
    result = []
    for item in string:
        if item not in result:
            result.append(item)
    return result
print(remove_duplicates([1, 1, 1, 1, 1]))

# Solution using set
def remove_duplicates(items):
    return list(set(items))


"""
Implement a function is_distinct() to check if the list contains unique
"""
def is_distinct(items):
    return len(items) == len(set(items))

""" 
Analyse the results of the functions below
"""
def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)
function(3)
function(5, ['a', 'b', 'c'])
function(6)

def function(*args, **kwargs):
    print(args, kwargs)
function(3,4)
function(x=3, y=4)
function(1, 2, x=3, y=4)


"""
Implement a function is_palindrome(), which takes as an argument 
str object and checks if the object is a palindrome

If so, the function should return True, on the contrary False
"""
def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False
print(is_palindrome('level'))

