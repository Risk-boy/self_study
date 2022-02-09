a, b = map(int, input().split())

end_sum = a + b 
len = b - a + 1
if a <= b:
    len = b - a + 1
    if (len % 2): 
        result = end_sum * (len // 2) + (end_sum // 2)
    else:
        result = end_sum * (len // 2)
elif a >= b:
    len = a - b + 1
    if (len % 2): 
        result = end_sum * (len // 2) + (end_sum // 2)
    else:
        result = end_sum * (len // 2)
print(result)
