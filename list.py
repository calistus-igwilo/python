"""
The following text is given:

    text = 'Python programming'
Standadize the text(replace uppercase letters with lowercase). Then create 
a list of uniqe characters in the text. Remove the space from this list and
sort from a to z. Print the list to the console.

Tip: You can use set to generate unique characters 
"""

text = 'Python programming'
text = text.lower().replace(' ', '')
text = list(set(text))
text.sort()
print(text)


"""
The following list is given:

    filenames = ['view.jpg', 'bear.jpg', 'ball.png']
Add the file 'phone.jpg' to the list at the beginning. Then delete the
file 'ball.png'. In response, print the filenames list to console

Expected result:

    ['phone.jpg', 'view.jpg', 'bear.jpg']
"""

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)


"""
The following list represents order ids for a given day:

    day1 = ['3984', '9042', '4829', '2380']
Using the appropriate method, extend the list to the next day
    day2 = ['4231', '5234', '1345', '2455']

Expected result:
    ['3984', '9042', '4829', '2380', '4231', '5234', '1345', '2455']
"""
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
next_day = day1+day2
print(next_day)


"""
The following tuple is given:
    techs = ('python', 'java', 'sql', 'aws')
Sort the tuple from a to z and print it to the console

Tip: Tuples are immutable. You have to create a new one

Expected result:
    ('aws', 'java', 'python', 'sql')
"""
techs = ('python', 'java', 'sql', 'aws')
sort = tuple(sorted(techs))
print(sort)


"""
The following list is given:

    hashtags = ['summer', 'time', 'vibes']
Using the appropriate method, combine the elements of the list with
the '#' character. Also add this sign to the beginning of the text
and print the result to the console as shown below:

Expected result

"""

hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))