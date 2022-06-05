"""
Two following tuples are given:

    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')
Combine these tuples into one as shown below and print result to console

('AAPL.US', 'IBM.US', 'MSFT.US', 'HD.US', 'GS.US', 'NKE.US')
"""
from itertools import count


dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = dji1 + dji2
print(result)


"""
The following tuples are given:

    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')
Nest these tuples into one tuple as shown below and print the result
to console

Expected result:
    (('AAPL.US', 'IBM.US', 'MSFT.US'), ('HD.US', 'GS.US', 'NKE.US'))
"""
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = (dji1, dji2)
print(result)


"""
Tuples are immutable. The following tuple is given:

    members = (('Kate', 23), ('Tom', 19))
insert a tuple ('John', 26) between Kate and Tom as shown belo. 
Print the result to the console

Tip: You have to create a new tuple

Expected result:
    (('Kate', 23), ('John', 26), ('Tom', 19))
"""

members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('John', 26), members[1])
print(members)


"""
The following is given:
    default = ('YES', 'NO', 'NO', 'YES', 'NO')
Using the appropriate method return the number of occurrences of the 
string 'YES' and print the result to the console as shown below

    Number of occurences: 2
"""

default = ('YES', 'NO', 'NO', 'YES', 'NO')
cnt = default.count('YES')
print(f'Number of occurences: {cnt}')


"""
Sort the given tuple (from A to Z)

    names = ('Monica', 'Tom', 'John', 'Michael')
Print the sorted tuple to the console as shown below


"""
names = ('Monica', 'Tom', 'John', 'Michael')

result = tuple(sorted(names))
print(result)


"""
The following tuple is given (name,age):

    info = (('Monica', 19), ('Tom', 21), ('John', 18))
Sort the tuple:
    - ascending by age
    - descending by age
And print the result to the console as shown below


"""

info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Ascending: {asc}')
print((f'descending: {desc}'))


"""
The following tuple is given:
    stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
Extract a ticker for Apple and print the result to the comsole.

Expected result:
    APPL.US
"""

stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
print(stocks[0][1][0])
