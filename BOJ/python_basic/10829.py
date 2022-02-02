# 2진수 변환 
def bin(num):
    if num <= 1:
        return str(num % 2)
    else: 
        return bin(num // 2) + str(num % 2)

num = int(input())

print(bin(num))
