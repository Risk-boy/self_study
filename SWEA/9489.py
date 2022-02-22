T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    ls = [list(map(int, input().split())) for i in range(n)]

    cnt = 0 

    for i in range(n):
        for j in range(m):
            