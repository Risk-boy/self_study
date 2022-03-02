from audioop import reverse


n = input()
ls = []
for num in n:
    ls.append(int(num))
ls.sort(reverse = True)
for i in range(len(ls)):
    print(ls[i], end='')