T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = [0] * 1001
    for _ in range(n):
        k, a, b = map(int, input().split())
        if k == 1:
            for i in range(a, b+1):
                result[i] += 1
        elif k == 2:
            for i in range(a, b, 2):
                result[i] += 1
            result[b] += 1
        elif k == 3:
            result[a] += 1
            result[b] += 1 
            for i in range(a+1, b):
                if not(a % 2) and not (i % 4):
                    result[i] += 1
                elif a % 2 and not(i % 3) and i % 10:
                    result[i] += 1
    maxV = max(result)
    print(f'#{tc} {maxV}')