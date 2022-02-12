chess = []

for i in range(8):
    T = list(input())
    chess.append(T)

total_white = 0 

for i in range(8):
    for j in range(8):
        if (i % 2 == 0) and (j % 2 == 0):
            if chess[i][j] == 'F':
                total_white += 1
        elif (i % 2 == 1) and (j % 2 == 1):
            if chess[i][j] == 'F':
                total_white += 1

print(total_white)