# import sys
# sys.stdin = open('input.txt')
# T = int(input())
#
# for order in range(1, T + 1):
#     N, M = map(int, input().split())
#     russia = [list(map(str, input())) for _ in range(N)]
#     result = N * M
#     one_count = 0
#     for w in range(0, N - 2):
#         for k1 in range(0, M):
#             if russia[w][k1] != 'W':
#                 one_count += 1
#         two_count = 0
#         if result <= one_count:
#             break
#         for b in range(1 + w, N - 1):
#             for k2 in range(0, M):
#                 if russia[b][k2] != 'B':
#                     two_count += 1
#             if result <= one_count + two_count:
#                 break
#             three_count = 0
#             for r in range(1 + b, N):
#                 for k3 in range(0, M):
#                     if russia[r][k3] != 'R':
#                         three_count += 1
#             if result > (one_count + two_count + three_count):
#                 result = (one_count + two_count + three_count)
#
#     print(f'#{order} {result}')
cl = ['W','B','R']
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    W = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    R = [0 for _ in range(N)]
    color = [[0 for _ in range(3)] for _ in range(N)]
    result = N*M
    for ind in range(N):
        W[ind] = M - flag[ind].count(cl[0])
        B[ind] = M - flag[ind].count(cl[1])
        R[ind] = M - flag[ind].count(cl[2])
    for w in range(1,N):
        for b in range(1, N-w):
            result = min(result, sum([sum(W[:w]),sum(B[w:w+b]), sum(R[w+b:])]))
    print('#%d'%test_case, result)

####
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    colors = [list(input()) for _ in range(n)]
    # 첫번째 마지막 줄 제외
    # 흰색은 1부터 n-3 인덱스까지
    # 파란색은 흰색 다음부터 n-2인덱스까지
    # 빨간색: 나머지
    min_value = 2500

    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0
            # 흰색
            for w in range(1, i+1):
                cnt += m - colors[w].count('W')
            # 파란색
            for b in range(i+1, j+1):
                cnt += m - colors[b].count('B')
            # 빨간색
            for r in range(j+1, n-1):
                cnt += m - colors[r].count('R')
            if cnt < min_value:
                min_value = cnt
    # 첫 줄, 마지막 줄 바꾸는 횟수
    a = m - colors[0].count('W')
    b = m - colors[-1].count('R')

    ans = a + b + min_value
    print(f'#{tc} {ans}')
