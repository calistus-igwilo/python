"""
In the Fibonacci sequence, each subsequent term is obtained by adding the preceeding
2 terms. This is true for all the numbers except the first 2 numbers of Fibonacci series
as they do not have 2 preceeding numbers. The first 2 terms in the Fibonacci series is
0 and 1. F(n) = F(n-1) + F(n-2) for n>1. Write a funtion that finds F(n) given n
where n is an integer greater than equal to0. For the first term n = 0.
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # Time complexity = O(2**n). Space complexity O(n)

print(f'fibonnaci: {fibonacci(6)}')

# Using memoization where values are stored in a hash table and referenced
def fibonacci(n):
    ht = {0:0, 1:1}
    if n in ht:
        return ht[n]
    else:
        ht[n] = fibonacci(n-1) + fibonacci(n-2)
        return ht[n]
    # Time complexity = O(n). Space complexity O(n)
print(f'fibonnaci optimized: {fibonacci(6)}')


# Method 3: Using a while loop
def fibonacci(n):
    if n <= 1:
        return n
    cnt = 1
    prev = 0
    current = 1
    while cnt < n:
        next = prev + cnt 
        prev = current 
        current = next 
        cnt += 1
    return current
    # Time complexity = O(n). Space complexity = O(1)
print(f'fibonacci loop: {fibonacci(8)}')


"""
Let's define a peculiar type of array in which each element is either an integer or
another peculiar array. Assume that a peculiar array is never empty. Write a function
that will take a peculiar array as its input and find the sum of its elements. If an 
array is an element in the peculiar array, you have to convert it to its equivalent
value so that you can sum it with the other elements. Equivalent value of an array
is the sum of its elements raised to the number which represents how far nested it is.
For e.g [2,3[4,1,2]] = 2+3+(4+1+2^2)
[1,2,[7,[3,4],2]] = 1+2+(7+(3+4)^3+2)^2
"""
def power_sum(arr, power=1):
    sum_ = 0
    for element in arr:
        if type(element) == list:
            sum_ += power_sum(element, power+1)
        else:
            sum_ += element
    return sum_ ** power

arr = [1,2,[4,1]]
print(power_sum(arr))