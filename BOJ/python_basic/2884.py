#알람 45분 전으로 맞추기 
H, M = map(int, input().split())

if H == 0:
    if M >= 45:
        print(0, M-45)
    else: 
        print(23, 15 + M)

else:
    if M >= 45: 
        print(H, M-45)
    else: 
        print(H-1, 15 + M)
    
