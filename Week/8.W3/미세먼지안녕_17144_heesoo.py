# 미세먼지안녕 17144
import sys
from collections import deque
r, c, t = map(int, sys.stdin.readline().split())
arr = []
cleaner = []
dx = [0,-1,0,1]
dy = [1,0,-1,0]
queue = deque()
for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(c):
        if temp[j] == -1:
            cleaner.append(i)
    arr.append(temp)

# bfs
def bfs():
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            temp[i][j] = arr[i][j]
            if arr[i][j] > 0:
                queue.append((i, j))
    
    while queue:
        cx, cy = queue.popleft()
        dust = arr[cx][cy]//5
        for i in range(4):
            nx, ny = cx + dx[i], cy+ dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                temp[nx][ny] += dust
                temp[cx][cy] -= dust

    for i in range(r):
        for j in range(c):
            arr[i][j] = temp[i][j]



def upCleaner():
    startX = cleaner[0]
    cx, cy = startX, 1
    prev = 0
    for i in range(4):
        while True:
            nx = cx + dx[i]
            ny = cy + dy[i]
            if cx == startX and cy == 0:  # 초기 위치에 도달한 경우 종료
                return
            if not (0 <= nx < r) or not (0 <= ny < c):  # 범위 밖이면 다음 방향으로
                break
            arr[cx][cy], prev = prev, arr[cx][cy]
            cx, cy = nx, ny
def downCleaner():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    startX = cleaner[1]
    cx, cy = startX, 1
    prev = 0
    for i in range(4):
        while True:
            nx = cx + dx[i]
            ny = cy + dy[i]
            if cx == startX and cy == 0:  # 초기 위치에 도달한 경우 종료
                return
            if not (0 <= nx < r) or not (0 <= ny < c):  # 범위 밖이면 다음 방향으로
                break
            arr[cx][cy], prev = prev, arr[cx][cy]
            cx, cy = nx, ny
    

for time in range(t):
    # 퍼트리기
    bfs()
    # 공기청정기
    upCleaner()
    downCleaner()

result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            result += arr[i][j]
print(result)