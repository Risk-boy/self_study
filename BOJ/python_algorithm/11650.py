n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

for k in range(n):
    print(arr[k][0], end=' ')
    print(arr[k][1])