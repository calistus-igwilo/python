def fizzBuzz(n):
    '''
    Given a number n, for each integer i in the range from 
    1 to n inclusive, print one value per line as follows:

    - if i is a multile of both 3 and 5 print FizzBuzz.
    - if i is a multiple of 3 (but not 5), print Fizz
    - if i is a multip of 5 (but not 3), print Buzz
    - if i is not a multiple of 3 or 5, print the value of i
    '''
    for i in range(1, n+1):
        if i%3 == 0 and n%5 == 0:
            print("FizzBuZZ")
        elif i%3 == 0 and i%5 != 0:
            print("Fizz")
        elif i%3 != 0 and i%5 == 0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(15)
