ls = []
for i in range(9):
    ls.append(int(input()))
total = sum(ls) - 100 
end = False

for i in range(len(ls)-1):
    if end:
        break
    for j in range(i+1, len(ls)):
        if  ls[i] + ls[j] == total:
            ls.pop(j)
            ls.pop(i)
            end = True
            break 

for num in ls:
    print(num)