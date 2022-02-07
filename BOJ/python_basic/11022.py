N = int(input())
i = N
while i > 0:
    a, b = map(int, input().split())
    result = a + b
    i -= 1
    j = N - i 
    print(f'Case #{j}: {a} + {b} = {result}')