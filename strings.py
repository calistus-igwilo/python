""" 
The folowing text is given:
    text = 'python is a popular programming language.'
Use the appropriate method to replace the first letter 
of the text with uppercase. Print the result to console
"""

from typing import Counter


text = 'python is a popular programming language.'
print(text.capitalize())

# Count the number of occurrences of the letter 'p' and
# print the result to the consle as shown
#    Number of occurrencies: 4

#cnt = Counter(text)
print(f"Number of occurences: {text.count('p')}")

# Check if string ends with a substring
"""
The following codes are given:
    code1 = 'FVNISJND-XX-2020'
    code2 = 'FVNISJND-XY-2019'

Using the appropriate method check if the codes end in '2020'.
Print the results to the console as shown below:
    code1: True
    code2: False

"""
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")

"""
The following paths are given:

path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
Using the appropriate method, find the word 'scientist' in the given paths,
returning the index for the first letter of the found word. If the word is
not in the path, the method should return -1. Print the result to the console
as shown below:

path1: 49
path2: 49
path3: -1
"""

path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'

print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")

# isalnum 
"""
The following codes are given:

    code1 = 'FVNISJND-20'
    code2 = 'FVNISJND20'
Using the appropriate method, check whether the codes consist only of
alphanumeric characters (numbers + letters). Print the result to 
the console as shown below:

    code1: False
    code2: True
"""
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f"code2: {code2.isalnum()}")

# strip()
"""
The following text is given:

    text = '  Google Colab   '
Using appropriate method, remove whitespace characters around the text.
Print the result to the console
"""
text = '  Google Colab   '
print(text.strip())

"""
The following text is given:

    txt = ",,,,,rrttgg.....banana....rrr"
Using appropriat method, remove the characters: ,.grt
Print the output to the console as shown below:
    
    banana
"""
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

# replace()
"""
The following code is given:

    code = 'FVNISJND-XX'
Using the appropriate method, replace the dash with a space.
Print the output to the console as shown below:

FVNISJND XX
"""
code = 'FVNISJND-XX'
print(code.replace('-', ' '))

# remove all dashes from the text below
text = '340-23-245-235'
print(text.replace("-", ''))

# split()
"""
The folowing text is given:

    text = 'Open,High,Low,Close'
Using the appropriate method split the text by comma. 
Print the result to the console as shown below:

    ['Open', 'High', 'Low', 'Close']
"""
text = 'Open,High,Low,Close'
print(text.split(','))


# The following text is given
#
#    text = """Python is a general-purpose language.
#    Python is popular."""
# Using appropriate method, split the text into sentences.
# print the result to the console as shown belos
#
# ['Python is a general-purpose language.', 'Python is popular']
#    

text = """Python is a general-purpose language.
Python is popular."""

print(text.strip('"').split('\n'))

"""
The following variable is given:

    num = 34
Using the appropriate method for an object of type str, print 
the variable num preceded by four zeros to console as shown:

    000034
"""
num = 34
print(str(num).zfill(6))


"""
From the given url:
    url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
extract the slug after the last character '/'. Then replace all dashes 
with spaces and print the result to console as shown below:
"""

url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
slug = url.split('/')[4] # or url.split('/)[-1]
print(slug.replace('-', ' '))
