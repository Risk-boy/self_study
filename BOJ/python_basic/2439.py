n = int(input())

for i in range(1, n):
    print(' ' * (n - i), end ='')
    print('*' * i)

print('*' * n, end ='')