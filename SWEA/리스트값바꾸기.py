n = int(input())
arr = list(map(int, input().split()))

arr[n] = 'change'

for i in range(len(arr)):
    print(arr[i], end=' ')