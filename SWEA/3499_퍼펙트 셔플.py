T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(str,input().split()))
    ls = [0] * n
    if n % 2 == 0:
        for i in range(n // 2):
            ls[2*i] = arr[i]
        for j in range(n // 2, n):
            ls[2*(j-(n//2)) + 1] = arr[j]
    else:
        for i in range(n // 2 + 1):
            ls[2*i] = arr[i]
        for j in range(n // 2 + 1, n):
            ls[2*(j-(n//2+1)) + 1] = arr[j]
    print(f'#{tc}', *ls)