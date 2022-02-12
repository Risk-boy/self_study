n = int(input())

cnt = 0 
total = 0
start = 1

while total < n:
    for i in range(start, n + 1):
        end = True
        total += i
        cnt += 1
        if total + (i+1) > n:
            start = 1
            end = False 
        if end == False:
            break

print(cnt)