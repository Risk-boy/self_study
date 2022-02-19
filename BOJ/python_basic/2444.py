n = int(input())

for i in range(1, 2 * n):
    if i <= n:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else: 
        print(' ' * (i - n) + '*' * (4 * n - 2 * i - 1)) # * 부분: 전체 2n-1 에서 공백길이 (i-n)을 두번 빼주기
