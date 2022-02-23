# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    # n명의 손님 m초의 시간동안 k개의 붕어빵
    n, m, k = map(int, input().split())
    # 손님 오는 시간
    arr = list(map(int, input().split()))
    cnt = 0 # 붕어빵 잔고
    ans = True  # flag 변수
    for i in range(0, 11112):   # 손님의 범위가 11111까지 이므로
        if i >= m and i % m == 0:   # 0에 대한 예외 처리를 위해 i>=m을 넣어줌
            cnt += k    # 붕어빵 갯수 추가
        if i in arr:
            cnt -= arr.count(i) # 손님이 먹은 붕어빵을 잔고에서 차감
        if cnt < 0: # 잔고가 0보다 작아진다면
            ans = False 
    if ans:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

# 교수님 풀이
# def func(n, m, k, lst):  # n = len(lst)
#     bucket = [0] * 11112

#     # 손님을 버켓에 등록
#     for item in lst:
#         bucket[item]-=1

#     # 누적합 구하면서 m초에 해당하는 인덱스에
#     # 도달하면.. 버켓의 값을 k개 증가
#     # 버켓의 값을 확인 하는데 음수다.. 그러면 꺼버리기
#     #
#     if bucket[0] < 0:  # 만약에 손님이 0초에도 온다면..
#          return 'Impossible'

#     for i in range(1, len(bucket)):
#         bucket[i] += bucket[i - 1] # 누적합
#         if i%m==0:
#             bucket[i]+=k
#         if bucket[i]<0:
#             return '불가능'
#     return '가능'

# t = int(input())
# for i in range(t):
#     n, m, k = list(map(int, input().split()))
#     lst = list(map(int, input().split()))
#     result = func(n, m, k, lst)
#     print(f'#{i + 1} {result}')