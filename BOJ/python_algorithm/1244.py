# 스위치 켜고 끄기

n = int(input()) # 스위치 갯수
arr = list(map(int, input().split())) # 스위치 상태 
m = int(input()) # 학생 수
for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1: # 남자인 경우
        for i in range(n):
            if (i + 1) % num == 0:  # 스위치 번호가 num의 배수
                arr[i] = (arr[i] + 1) % 2   # 0은 1로, 1은 0으로 바꿔주기
    elif gender == 2: # 여자인 경우
        max_len = 0 # 최대 길이를 위한 변수
        my_len = 0  # 좌우 대칭일 때 구한 길이
        for j in range(num):
            if 2*(num-1)-j < n and arr[j:2*num-j-1] == arr[j:2*num-j-1][::-1]:  # 인덱스 범위를 벗어나지 않으면서 좌우 대칭일 때
                my_len = 2 * (num-j)-1  # 길이 구하기
                if my_len > max_len:    # 최대 길이 구하기
                    max_len = my_len
        for k in range(num - 1 - (max_len - 1) // 2, num + (max_len - 1) // 2): # 기준점으로부터 좌우로 스위치 변경
            arr[k] = (arr[k] + 1) % 2

for i in range(n):
    if (i + 1) % 20 == 0:   # 21번째 부터 줄 바꿈
        print(arr[i], end=' ')
        print()
    else: 
        print(arr[i], end=' ')
