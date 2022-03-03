# 연속구간
for _ in range(3):
    nums = list(input())
    max_cnt = 1 
    for i in range(0, 8):
        cnt = 1
        j = 1
        while j < 8 and i + j < 8 and nums[i] == nums[i+j]:
            cnt += 1
            j += 1
        if cnt > max_cnt:
            max_cnt = cnt 
    print(max_cnt)
