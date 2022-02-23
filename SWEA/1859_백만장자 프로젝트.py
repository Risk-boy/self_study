import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    max_num = nums[-1]
    for i in range(n-2, -1, -1):    # 뒤에서 앞으로 오면서
        if max_num < nums[i]:   # max_num보다 크다면 max값 갱신
            max_num = nums[i]
        else:
            ans += max_num - nums[i]    # 작다면 사서 팔 것이기 때문에 빼서 차익만 ans에 더해주기

    print(f'#{tc} {ans}')

# 교수님 풀이
# T = int(input())

# for tc in range(1, T + 1):
#     n = int(input())
#     price = list(map(int, input().split()))

#     max = price[-1]  # 801
#     profit = 0
#     for i in range(n - 2, -1, -1):
#     # 현재가가 최고가보다 크다면 최고가 갱신
#         if price[i] >= max:
#             max = price[i]
#             # 현재가가 최고가보다 작다면
#             # 최고가 - 현재가 이익 누적시키기
#         else:
#             profit += max - price[i]

#     print("#{0} {1}".format(tc, profit))