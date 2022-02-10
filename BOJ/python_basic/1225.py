a, b = input().split()

total_a = 0
total_b = 0 
for i in a:
    total_a += int(i)
for i in b:
    total_b += int(i)
total = total_a * total_b
print(total)