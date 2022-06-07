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


"""
Write a program that checks if the given number is a prime number
(use the break statement)
    number = 13
Print one of the following to the console depending on the result
    13 - prime number
    13 - not a prime number

Expected result
    13 - prime number
"""
number = 13
if number > 1:
    for i in range(2, number):
        if number% i == 0:
            print(f'{number} - not a prime number')
            break
    else:
        print(f'{number} - prime number')