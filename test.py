nums = [2,1,2,3,5]
missing = [num for num in range(1, len(nums)+1) if num not in nums]
duplicate = [num for num in nums if nums.count(num)>1]
result = (duplicate[1], missing[0])
print(result)

