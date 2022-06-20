from curses.ascii import isdigit


nums = [2,1,2,3,5]
missing = [num for num in range(1, len(nums)+1) if num not in nums]
duplicate = [num for num in nums if nums.count(num)>1]
result = (duplicate[1], missing[0])
print(result)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [(i, j) for i in a for j in b]
for i in result:
    print(i, end=" ")

s, num = input().split()
print(f's: {s}, num: {num}')

