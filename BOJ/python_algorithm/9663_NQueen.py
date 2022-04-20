
def dfs(n):
    global ans 
    if n == N:
        ans += 1
        return

    for i in range(N):
        if v1[i] == v2[i-n] == v3[i+n] == 0:
            v1[i] = v2[i-n] = v3[i+n] = 1
            dfs(n+1)
            v1[i] = v2[i-n] = v3[i+n] = 0




N = int(input())
v1 = [0] * N        # 세로방향 확인 
v2 = [0] * (2*N-1)  # 2,4분면 확인
v3 = [0] * (2*N-1)  # 1,3분면 확인
ans = 0 
dfs(0)

print(f'{ans}')