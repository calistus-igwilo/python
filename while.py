"""
Write a program that prints to the console the first ten prim numbers
separated by comma

Tip: use the while loop with break statement
Expected result
    2,3,5,7,11,13,17,19,23,29
"""
counter = 0
number = 2
prime = []
while counter < 10:
    for i in range(2, number):
        if number%i == 0:
            break
    else:
        prime.append(str(number))
        counter +=1
    number +=1
print(','.join(prime))


"""
Using the while loop, calculate how many years you have to wait for the
return on the investment described below to at least double your 
money (we only take into account full periods).

Description
    n - number of periods (in years)
    pv - present value
    r - interest rate (annual)
    fv - future value

Invstment paramenters
    pv = 1000
    r = 0.04
Print result tothe console as shown below:
    Future value: 2025.82 USD. Number of period: 18 years
"""
pv = 1000
r = 0.04
fv = pv * (1 + r)
n = 1
while fv <= 2000:
    fv = fv * (1+r)
    n += 1
print(f'Future value: {fv :.2f} USD. Number of period: {n} years')


"""
Write a program that checks if the given element (target) is in the 
sorted list (numbers). Given:
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 7

Algorithim:

1. We set the<em> start</em> and <em>end </em>index as well as the flag = None

2. As long as the start index is not greater than the end index, select the 
middle index mid of the list (arithmetic average of the start and end index => 
remember to convert the result with the int() function). If the start index 
is greater than the <em>end</em> index, we end the algorithm.

3. Check if the element for the index calculated in this way is our target. 
If so, we set the flag to True and terminate the algorithm. If not => step 4.

4. We check if the element of the list for the index mid is less than the target. If so, we increase the start index by 1. If not, we reduce the end index by 1 and go to step 2.After while loop, depending on the value of the flag, print to the console:'Found' or 'Not found'
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
 
if flag:
    print('Found')
else:
    print('Not found')
