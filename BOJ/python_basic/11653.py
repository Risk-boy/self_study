n = int(input())

nums = list(range(2, n+1))

for i in range(n-1):
    while n % nums[i] == 0:
        print(nums[i])
        n //= nums[i]