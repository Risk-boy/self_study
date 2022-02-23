n = int(input())
scores = list(map(int, input().split()))
max_scores = max(scores)
ans = sum(scores)/max_scores/n*100 
print(ans)
