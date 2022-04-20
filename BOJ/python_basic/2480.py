nums = list(map(int, input().split()))
nums.sort()
ans = 0
if nums[0] == nums[1] == nums[2]:
    ans = 10000 + nums[0] * 1000
elif nums[0] == nums[1] and nums[1] != nums[2]:
    ans = 1000 + nums[0] * 100
elif nums[0] != nums[1] and nums[1] == nums[2]:
    ans = 1000 + nums[1] * 100
elif nums[0] != nums[1] and nums[1] != nums[2]:
    ans = nums[2] * 100
print(ans)
