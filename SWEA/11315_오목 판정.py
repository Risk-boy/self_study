# 오목 판정
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    end = False
    # 가로 
    ans = False  # flag 변수
    for r in range(n):
        for c in range(0, n):
            if c+5 <= n and arr[r][c:c+5] == ['o','o','o','o','o']:
                end = True
    # 대각선
    for r in range(n):
        for c in range(0, n):
            if c+5 <= n and r+5 <= n and arr[r][c] == 'o' and arr[r+1][c+1] == 'o' and arr[r+2][c+2] == 'o' and arr[r+3][c+3] == 'o' and arr[r+4][c+4] == 'o':
                end = True
    for r in range(n):
        for c in range(n-1, -1, -1):
            if c-5 >= -1 and r+5 <=n and arr[r][c] == 'o' and arr[r+1][c-1] == 'o' and arr[r+2][c-2] == 'o' and arr[r+3][c-3] == 'o' and arr[r+4][c-4] == 'o':
                end = True
    # 세로 
    arr_T = list(map(list, zip(*arr)))
    for r in range(n):
        for c in range(0, n):
            if c+5 <= n and arr_T[r][c:c+5] == ['o','o','o','o','o']:
                end = True

    if end:
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'#{tc} {ans}')


