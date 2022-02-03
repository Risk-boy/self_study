a = int(input())
b = int(input())
c = int(input())

n = a * b * c

num = str(n)

ls = [0] * 10 
for i in num:
    for j in range(10):
        if i == str(j):
            ls[int(i)] += 1

for i in ls:
    print(i)
