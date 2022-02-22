T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input()))

    max_value = 0
    cnt = 0 

        
    for i in range(n):
        if nums[i] == 1:
            cnt += 1
            if cnt > max_value:
                max_value = cnt
            else: 
                cnt = 0

    print('#{} {}'.format(tc, max_value))

