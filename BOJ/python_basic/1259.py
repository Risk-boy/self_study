while True:
    nums = list(input())
    n = len(nums)
    flag = 'yes'
    if nums[0] == '0':
        break
    if n % 2 == 0:
        for i in range(n//2):
            if nums[i] != nums[n-1-i]:
                flag = 'no'
    elif n % 2 == 1:
        for i in range(n//2):
            if nums[i] != nums[n-1-i]:
                flag = 'no'
    print(flag)


