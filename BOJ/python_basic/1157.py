word = input()
new_word = word.upper()

ls = [0] * 91
for element in new_word:
    ls[ord(element)] += 1
ans = 0
maxNum = max(ls)
if ls.count(maxNum) >= 2:
    ans = '?'
else:
    maxIndex = ls.index(maxNum)
    ans = chr(maxIndex)

print(ans)
