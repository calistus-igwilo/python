"""
Find the sum of all numbers that are divisible by 5 or 7 less than 100.
Present the solution in the form of calculate(). In response, call 
calculate() function and print the result to the console.

Expected result:
    1580
"""
from pickle import FALSE


def calculate():
    sum_ = 0
    for n in range(100):
        if n%5 == 0 or n%7 == 0:
            sum_ += n
    return(sum_)
print(calculate())


# Fibonaci
"""
Consider the Fibonaci sequence. It is a sequence of natuarl numbers 
defined recursively as follows:
    - the first element of the sequence is 0
    - the second element of the sequence is 1
    - each next element of the sequence is the sum of the previous two elements.
The begining of the Fibonaci sequence:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Find the sum of all the even elements of the Fibonaci sequence with vlaues
less than 1,000,000(1million) 

Expected result:
    1089154
"""

def fibonaci_even():
    a = 0
    b = 1
    total = 0
    while a < 1000000:
        if a%2 == 0:
            total += a
        a, b = b, a + b
    return total
print(fibonaci_even())

"""
Check if a number is a prime number
"""
def isprime(num):
    isprime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                isprime = False
                break
    return isprime
print(f'isprime {isprime(2)}')





 


