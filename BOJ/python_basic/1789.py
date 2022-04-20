S = int(input())

n = int((S * 2)**0.5)
print(n)
if (n)*(n+1)//2 < S:
    print(n)
else:
    print(n+1)
