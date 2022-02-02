ls = []
for num in range(9):
    a = int(input())
    ls.append(a)

max_num = max(ls)
for i in range(len(ls)):
    if max_num == ls[i]:
        max_index = i + 1 
print(max_num)
print(max_index)

