# 분해합
n = int(input())

end = False

for i in range(1, n):
    a = i
    b = i
    c = i
    while b >= 10:
        a += b % 10
        b //= 10 
    a += b
    if a == n: 
        end = True
        break
if not end:
    print(0)
else: 
    print(c)