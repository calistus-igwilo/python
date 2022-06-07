"""
Write a program that compares two lists and returns True if the list
contains at least one of the same element. Otherwise, it will return
False.
Use break statement in the solution and print result to the console
List:
   list1 = [1, 2, 0]
    list2 = [4, 5, 6, 1] 
"""
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

result = False
for item1 in list1:
    if item1 in list2:
        result = True
        break
print(result)


"""
The following list of hashtags is given:

    hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
Check if all object in the list are of str type. If so, print True, 
otherwise print False. Use the break statement in the solution
"""
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True
for item in hashtags:
    if not type(item) == str:  # if not isinstance(item, str):
        result = False
        break
print(result)

