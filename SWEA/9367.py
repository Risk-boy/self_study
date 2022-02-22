T = int(input())
for tc in range(1, T+1):    
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 1
    max_cnt = 0
    for i in range(n-1):
        if nums[i] < nums[i+1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else: 
            cnt = 1

    print('#{} {}'.format(tc, max_cnt))