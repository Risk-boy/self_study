remainders = set()
for _ in range(10):
    remainders.add(int(input()) % 42)

ans = len(remainders)
print(ans)