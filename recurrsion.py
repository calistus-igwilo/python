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
Sum of power:
"""
def power_sum(arr, power=1):
    sum = 0
    for element in arr:
        if type(element) == arr