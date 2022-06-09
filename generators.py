##########################
# GENERATORS
##########################
"""
Implement a generator named file_gen(), which selects only those names
of files with the '.txt' extension from the list
"""
def file_gen(names):
    for name in names:
        if name.endswith('.txt'):
            yield name
names = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
print(list(file_gen(names)))


"""
Implement a generator called enum() that works just like the enumerate()
built-in function. For simplicity, the function gets an iterable object 
and returns a tuple(index, element)

Example:
Given: ['TEN', 'CDR', 'BBT']
Result: [(0, 'TEN'), (1, 'CDR'), (2, 'BBT')]
"""
def enum(objects):
    idx = 0
    for object in objects:
        yield (idx, object)
        idx += 1
print(list(enum(['TEN', 'CDR', 'BBT'])))


"""
Implement a generator named dayname() that accepts the index of the 
element from the following list:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
and allows us to iterate over 3 days (previous day, present day, next day)
"""
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7]
print(list(dayname(6)))


