n = int(input())

arr = [3 * i for i in range(1, n+1)]

for i in range(n-1, -1, -1):
    print(arr[i], end=' ')