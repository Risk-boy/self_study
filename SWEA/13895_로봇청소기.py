# d 0 1 2 3 북 동 남 서 
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0] # 북, 동, 남, 서 방향 
dc = [0, 1, 0, -1]

cnt = 0 
flag = True

while flag:
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    
    for _ in range(4):  # 4방향 체크 
        if d == 0: 
            d = 3
        else:
            d -= 1
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc] == 0: # index범위랑 빈공간 체크
            r, c = nr, nc 
            break 
    else: 
        nr = r + dr[(d+2) % 4]
        nc = c + dc[(d+2) % 4]
        if arr[nr][nc] == 2:
            r, c = nr, nc
        else:
            flag = False
print(cnt)



# # 교수님 풀이
# n, m = map(int, input().split())  # arr 배열 크기
# y, x, d = map(int, input().split()) # 좌표 방향   0 북 1 동 2 남 3 서
# arr = [list(map(int, input().split())) for _ in range(n)]

# dy=[-1,0,1,0]   # 북 동 남 서    기준 1,1
# dx=[0,1,0,-1]

# ny=[1,0,-1,0]   # 로봇 청소기의 뒤를 보기 위한 좌표
# nx=[0,-1,0,1]

# answer=1  # 청소기 놓자마자 일단 1개 청소
# arr[y][x]=3  #  청소 한 곳은 1이라고 체크
# check=0   # 방향체크  # 왼쪽으로 돌면서 체크

# while 1:
#     if d==0:    # 왼쪽으로 돌기 때문에.. 북쪽 다음에는 서쪽..
#         d=3
#     else:
#         d-=1
#     if arr[y+dy[d]][x+dx[d]]==0:  # 왼쪽으로 봤는데 청소 아직 안했으면
#         y+=dy[d]                    # 기준 좌표값 바꿔주고 (이동)
#         x+=dx[d]
#         arr[y][x]=3         #청소하기
#         answer+=1           # 청소 횟수 올려주기
#         check=0             # 방향체크는 0으로 바꾸기
#     else:
#         check+=1

#     if check==4:
#         if arr[y+ny[d]][x+nx[d]]==1:   # 뒤가 벽이라면..
#             break
#         elif arr[y+ny[d]][x+nx[d]]==0:  # 뒤가 비어 있다면
#             y += ny[d]  # 기준 좌표값 바꿔주고 (이동)
#             x += nx[d]
#             arr[y][x] = 3  # 청소하기
#             answer += 1  # 청소 횟수 올려주기
#             check = 0
#         else:   # 이미 뒤가 비어있지 않고 청소한 곳이라면
#             y+=ny[d]
#             x+=nx[d]
#             check=0

# print(answer)

# # 수린님 풀이
# T = 1

# dr = [0, 1, 0, -1]
# dc = [-1, 0, 1, 0]

# for tc in range(1, T + 1):
#     total = 0
#     N, M = map(int, input().split()) # 방 세로, 가로
#     r, c, d = map(int, input().split()) # 로봇 청소기 현재 위치, 방향
#     room = [list(map(int, input().split())) for _ in range(N)]
#     nr = r # while문에서 현재 방부터 청소하기 위해 넣어줌
#     nc = c

#     while True:
#         # 내가 가려는 방향이 청소가 안 되어있다면 좌표 갱신하고 그 칸에 2로 표시
#         if room[nr][nc] == 0: 
#             r = nr
#             c = nc
#             room[r][c] = 2
#             total += 1

#         # 만약 현재 위치에서 사방이 청소되어있다면
#         if room[r][c + 1] and room[r][c - 1] and room[r + 1][c] and room[r - 1][c]:
#             # 내 뒤쪽이 벽이면 청소 중지
#             if room[r+dr[(d + 2) % 4]][c+dc[(d + 2) % 4]] == 1:
#                 break
#             # 후진할 수 있으면 후진
#             elif room[r+dr[(d + 2) % 4]][c+dc[(d + 2) % 4]] == 2:
#                 r += dr[(d+2) % 4]
#                 c += dc[(d + 2) % 4]
#                 continue # 이렇게 해주지 않으면 나의 현재 위치와 방향이 변함

#         d = (d + 1) % 4 # 한 번 움직일 때마다 방향이 바뀜

#         nr = r + dr[d]
#         nc = c + dc[d]

#     print(total)

# # 영주님 풀이 
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(N)]

# dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
# dc = [0, 1, 0, -1]

# counting = 0
# flag = 0

# while flag == 0:
#     # 1. 청소
#     if room[r][c] == 0:
#         room[r][c] = 3
#         counting += 1

#     # 2. 이전 값이 아닌 동안에 청소할 공간 찾을 때까지 이동
#     for _ in range(4):
#         d = 3 if d == 0 else d - 1  # d 이동하면서 다음 장소 확인
#         if room[r + dr[d]][c + dc[d]] == 0:  # 청소할 공간 찾았다!
#             r = r + dr[d]
#             c = c + dc[d]
#             break

#         # 못 찾았으면 한 번 더 왼쪽으로 이동


#     else:  # 청소할 공간 못 찾았다.  # d는 원래의 값인 상태.
#         # 4. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우, 작동 중지
#         if room[r - dr[d]][c - dc[d]] == 1:
#             flag = 1
#         # 3. 바라보는 방향을 유지한 채로 한 칸 후진
#         else:  # 뒤로 이동이 가능하다면, 이동
#             r = r - dr[d]
#             c = c - dc[d]

# print(counting)





















