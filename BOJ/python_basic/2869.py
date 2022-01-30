# #달팽이 나무오르기 
# 시간초과 나온 코드 
# u, d, tree = map(int, input().split())

# cnt = 0
# if u >= tree:
#     cnt = 1 
# while tree > 0: 
#     if tree - u <= 0:
#         cnt += 1 
#         break
#     else: 
#         tree = tree - u + d 
#         cnt += 1

# print(cnt)
# 이것 역시 시간초과...
# u, d , tree = map(int, input().split())

# n = 1 
# while True:
#     if n * u - (n-1) * d >= tree:
#         break
        
#     else: 
#         n += 1 

# print(n)
import math
u, d , tree = map(int, input().split())
print(math.ceil((tree-u)/(u-d)) + 1)

