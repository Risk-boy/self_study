n, m = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for _ in range(n):
    data = list(map(int, input().split()))
    for r in range(data[0] - 1, data[2]):
        for c in range(data[1] - 1, data[3]):
            arr[r][c] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > m:
            cnt += 1
print(cnt)