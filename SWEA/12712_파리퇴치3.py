T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0 # 최대값 변수 초기화
    # 십자가 방향
    dr = [-1, 0 ,1, 0]
    dc = [0, 1, 0, -1]
    for r in range(n):
        for c in range(n):
            result = arr[r][c]
            for k in range(4):
                for z in range(1, m):
                    nr = r + dr[k] * z
                    nc = c + dc[k] * z
                    if 0 <= nr < n and 0 <= nc < n:
                        result += arr[nr][nc]
            if maxV < result:
                maxV = result
    # 대각선 방향
    dr_x = [1, 1, -1, -1]
    dc_x = [1, -1, -1, 1]
    for r in range(n):
        for c in range(n):
            result_x = arr[r][c]
            for k in range(4):
                for z in range(1, m):
                    nr_x = r + dr_x[k] * z
                    nc_x = c + dc_x[k] * z
                    if 0 <= nr_x < n and 0 <= nc_x < n:
                        result_x += arr[nr_x][nc_x]
            if maxV < result_x:
                maxV = result_x
    print(f'#{tc} {maxV}')