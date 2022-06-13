"""
Consider the two-roll of the dice. Create the probability space (omega) and count the 
probabioity of getting a sum of points higher than 10. Use set comprehension
"""
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
#filter_pair = {pair for pair in omega if pair[0]==1 and pair[1]==2}
#print(f'filter {filter_pair}')
#print(f'Omega: {omega}')
#print(f'Pair:  {sum_gt_10}')
#print(f'lenth of Omega: {len(omega)}')
print(f'Probability: {len(sum_gt_10) / len(omega):.2f}')


"""
The following text is given:
    desc = "Playway: Playway is a producer of computer games."
Change all characters to lowercase, remove colon, period and then split the text into
words. Create a set of unique words and print the lenght of this set to the console
"""
desc = "Playway: Playway is a producer of computer games."
transform = desc.lower().replace(':', '').replace('.', '').split()
result = len(list(set(transform)))
print(result)


"""
Consider the two-roll of the dice. Create the probability space(omega) and calculate
the probability of getting a sum of squares higher or equal to 45. Use set comprehension
Round the reuslt to two decimal places and print the result to the console.
"""
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_sq = {sum for sum in omega if sum[0]**2 + sum[1]**2 >= 45}
probility = len(sum_sq)/len(omega)
print(f'Probability: {probility :.2}')


"""
Consider a three-roll of the dice. Create the probability space (omega) and calculate
the probability of obtaining three values which the sum is divisible by 7. Use set
comprehension. Round result to two decimal places and print the result to the console
"""
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
sum_ = {(i, j, k) for i, j, k in omega if (i+j+k)%7 == 0 }
print(f'Probability: {round(len(sum_) / len(omega), 2)}')


"""
Calculate the probability that in three throws of symmetrical cubic dice, the sum of 
the squares of points will be divisible by 3. Use set comprehension. Round the result
to the fourth decimal place and print the result to the console. 
"""
sum_sq = {(i, j, k) for i, j, k in omega if (i**2 + j**2 + k**2)%3 == 0}
prob = round(len(omega) / len(sum_sq), 4)
print(f'Probability of squares: {prob}')


"""
We roll the symmetrical dice three times. Calculate the probabioity of the follwing:
    odd number of points in each roll
Use set comprehension. Round the result to three decimal places and print to console
"""
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
odd = {(i, j, k) for i, j, k in omega if i%2 ==1 and j%2 ==1 and k%2 ==1}
print(f'Odd numbers: {odd}')
prob = round(len(odd)/len(omega), 3)
print(prob)


"""

"""