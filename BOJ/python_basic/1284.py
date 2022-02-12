nums = [4, 2] + [3] * 8
while True:
    n = input()
    if n == '0':
        break
    print(sum([nums[int(num)] + 1 for num in n]) + 1)