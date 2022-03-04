x, y = input().split()

def Rev(num):
    ls = [] 
    if len(num) == 1:
        ls.append(num)
    elif len(num) == 2:
        if num[1] != '0':
            for i in range(1,-1,-1):
                ls.append(num[i])
        elif num[1] == '0':    
            ls.append(num[0])
    elif len(num) == 3:
        if num[2] != '0':
            for i in range(2, -1, -1):
                ls.append(num[i])
        elif num[2] == '0':
            if num[1] != '0':
                for i in range(1,-1,-1):
                    ls.append(num[i])
            elif num[1] == '0':
                ls.append(num[0])
    elif len(num) == 4:
        if num[3] != '0':
            for i in range(3,-1,-1):
                ls.append(num[i])
        elif num[3] == '0':
            if num[2] != '0':
                for i in range(2, -1, -1):
                    ls.append(num[i])
            elif num[2] == '0':
                if num[1] != '0':
                    for i in range(1,-1,-1):
                        ls.append(num[i])
                elif num[1] == '0':
                    ls.append(num[0])
    return ls 

a = ''.join(Rev(x))
b = ''.join(Rev(y))
c = int(a) + int(b)
d = str(c)
e = ''.join(Rev(d))
print(e)
