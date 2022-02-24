n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    r, c, x, y = data[0], data[1], data[2], data[3]
    ans = 0
    for i in range(r-1, x):
        for j in range(c-1, y):
            ans += arr[i][j]
    print(ans)