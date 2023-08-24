#7569 토마토
# 1: 익은 토마토, 0: 익지않은 토마토, -1: 토마토가 들어있지않은칸
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
queue = deque()
# h 개수만큼 배열 만들기
arr = [[[]*M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        arr[h][n] = temp
        for m in range(M):
            if temp[m] == 1:
                queue.append((h, n, m)) # 익은 토마토 들어있으면 큐에 넣기

# 기존 탐색 그래프에서 방향만 추가해주면됨
# 상하좌우 위아래
dz = [0, 0, 0, 0, -1, 1] # H
dx = [-1, 1, 0, 0, 0, 0] # N
dy = [0, 0, -1, 1, 0, 0] # M

day= 0
while queue:
    cz, cx, cy = queue.popleft() # 익은토마토 꺼내기

    for i in range(6):
        nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
        # 범위안에 있고 아직 방문하지 않은곳이면
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and arr[nz][nx][ny]==0:
            queue.append((nz, nx, ny))
            arr[nz][nx][ny] = arr[cz][cx][cy] + 1

day = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 0:
                print(-1)
                exit(0)
            day = max(day, arr[z][x][y])
print(day-1)
