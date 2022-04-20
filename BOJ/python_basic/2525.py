hour, minute = map(int, input().split())
time = int(input())
t1 = time // 60
t2 = time % 60
minutes = t2 + minute
ans1 = ans2 = 0
if minutes < 60:
    ans2 = minutes
    if hour + t1 < 24:
        ans1 = hour + t1
    else:
        ans1 = (hour + t1) % 24
else:
    excess_minutes = minutes // 60
    remain_minutes = minutes % 60
    ans2 = remain_minutes
    if hour + t1 + excess_minutes < 24:
        ans1 = hour + t1 + excess_minutes
    else:
        ans1 = (hour + t1 + excess_minutes) % 24
print(f'{ans1} {ans2}')


