# 1913 달팽이
import sys

N = int(sys.stdin.readline()) # 홀수
num = int(sys.stdin.readline()) # 위치를 찾고자하는수
posY, posX = 0, 0
board = [[0]*N for _ in range(N)]
# 출발점 (0,0)에서 시작해서 거꾸로 채워나가기
direction = [(1,0), (0,1), (-1,0), (0,-1)] # 아래, 오른쪽, 위, 왼쪽
cy, cx = (0,0)
dir = 0
for k in range(N*N,0,-1):
    if k == num:
        posY, posX = cy+1, cx+1
    board[cy][cx] = k # 현재 위치에 숫자 기록
    ny, nx = cy + direction[dir][0], cx + direction[dir][1] # 다음 위치 구하기
    if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 0 : # 방향 꺾어야하는 시점
        dir = (dir+1)%4
    
    cy, cx = cy + direction[dir][0], cx + direction[dir][1] # 다음 위치로 넘어가기
        

for i in board:
    for k in i:
        print(k, end=' ')
    print()
print(posY, posX)