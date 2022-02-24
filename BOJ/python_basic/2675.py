T = int(input())
for _ in range(T):
    n, word = input().split()
    for char in word:
        print(char*int(n), end='')
    print()