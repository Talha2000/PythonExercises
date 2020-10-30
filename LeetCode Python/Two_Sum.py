def twoSum(nums, target):
    ans = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in ans:
            return [ans[remaining],i]
        else:
            ans[num] = i
            
    

print(twoSum([2,7,11,17], 9))      