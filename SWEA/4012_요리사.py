# def combination(arr, r):
#     # 1.
#     arr = sorted(arr)

#     # 2.
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#         # 3.
#         if chosen:
#             start = arr.index(chosen[-1]) + 1
#         else:
#             start = 0 
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#     generate([])
from itertools import combinations
import sys 
sys.stdin = open('input.txt')
T = int(input()) 
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_T = list(map(list, zip(*arr)))
    ls_1 = list(combinations(list(range(n)), n // 2))
    ls_2 = [] 
    for i in range(len(ls_1)):
        ls = list(range(n))
        for j in ls_1[i]:
            ls.remove(j)
        ls_2.append(ls)

    food = 0
    min_food = 320000
    for i in range(len(ls_1)):
        food_1 = 0 
        food_2 = 0
        for j in range(n//2-1):
            for k in range(j+1, n//2):
                food_1 += arr[ls_1[i][j]][ls_1[i][k]] + arr_T[ls_1[i][j]][ls_1[i][k]]
                food_2 += arr[ls_2[i][j]][ls_2[i][k]] + arr_T[ls_2[i][j]][ls_2[i][k]]
        food = abs(food_1 - food_2)
        if min_food >= food:
            min_food = food 
    print(f'#{tc} {min_food}')