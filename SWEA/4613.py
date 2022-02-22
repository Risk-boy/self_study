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