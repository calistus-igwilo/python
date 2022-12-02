"""
Write a program that finds all two-digit numbers divisible by 11 
(use a for loop). Print the result to the console as comma-separated
values as shown

    11,22,33,44,55,66,77,88,99
"""
numbers = []
for num in range(1, 100):
    if num % 11 == 0:
        numbers.append(str(num))
result = ','.join(numbers)
print(result)


"""
The following list of numbers is given:
    items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
Write a program that removes odd numbers and returns the remaining ones.
Print the result to the console

Expected result:
    [4, 6, 10, 24]
"""
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if item % 2 == 0:
        result.append(item)
print(result)


"""
The following is given:
    items = [1, 5, 3, 2, 2, 4, 2, 4]
Write a program that removes duplicates from the list (the order must 
be kept) and print the list to the console

Expected result
[1, 5, 3, 2, 4]
"""
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
for item in items:
    if not item in result:
        result.append(item)
print(result)


"""
The following list is given:

text = 'Python is a very popular programming language'
Write a program which extracts exactly the first four words as a list.
Standardize each work, i.e replace uppercase leters with lowercase.
Present the result in a list and print to the console as shwon below
"""
text = 'Python is a very popular programming language'
counter = 0
result = []
for char in text:
    if char == ' ':
        counter += 1
        if counter == 4:
            break
    result.append(char.lower())
    words = ''.join(result).split()
print(words)

# Another solution using enumarate
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)


"""
Consider the problem of binary classification in machine learning. 
The machine learning model returns the probability of belonging to 
the class. If it's less than 0.5, the sample is assigned to class 0,
otherwise to class 1.

A list of probabilities from the machine learning model is given:

    probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
Write a program that assigns class 0 for values less than 0.5 and 1 for
valuies greater than or equal to 0.5. Print the result to the console

Expected result:
    [0, 1, 0, 1, 1, 0]
"""
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for num in probabilities:
    if num < 0.5:
        result.append(0)
    else:
        result.append(1)
print(result)


"""
Write a program that creates a histogram as a dictionary of the 
following values:
    items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
In response, print the histogram to the console
"""
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
dic = {}
for char in items:
    if not char in dic:
        cnt = items.count(char)
        dic[char] = cnt
print(dic)


"""
The following text is given:

text = '''Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would 
rather not use anything else'''

Create a list of words from the given text. Then standardize this text
(change uppercase letters to lowercase, remove punctuation marks).
Extract words longer than six characters and print the result to console

Expected result
    ['powerful', 'everywhere', 'friendly', 'reasons', 'anything']
"""
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

words = text.lower().strip().replace('.', '').split()
result = []
for word in words:
    if len(word) > 6:
        result.append(word)
print(result)

# Another solution using list comprehension
words = text.lower().strip().replace('.', '').split()
words = [word for word in words if len(word) > 6]
print(words)


"""
A dictionary of companies from the WIG.GAMES index is given. The key is
the 3-ltter company ticker and value - close price.

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
Iterate through this dictionary and print the tickers of those companies
where closing price is greater than 100.00 PLN.

Expected result:

"""
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for ticker, close in gaming.items():
    if close > 100.00:
        print(ticker)


    

