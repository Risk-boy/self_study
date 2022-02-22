T = int(input())
for tc in range(1, T+1):
    # n명의 손님 m초의 시간동안 k개의 붕어빵
    n, m, k = map(int, input().split())
    # 손님 오는 시간
    arr = list(map(int, input().split()))
    arr.sort()
    boong = [0] * len(arr)
    
    for i in range(len(boong)):
        if (i + 1) % m == 0:
            for j in range(i,i+j):
                boong[j] += 1
    
    end = True
    for i in range(0, n):
        if arr[i] < m:
            end = False
        elif boong[arr[i]-1] == 0:
            end = False
    if end:
        print('possible')
    else:
        print('impossible')

