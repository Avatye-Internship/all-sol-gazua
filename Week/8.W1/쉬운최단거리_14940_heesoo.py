# 14940 쉬운최단거리
# 0: 갈수없는땅, 1: 갈수있는땅, 2: 목표지점
# 각 지점에서 목표지점까지의 거리

# 목표지점에서 bfs 시작
# 시작지점 방문처리, 큐에 넣기, 결과에 count = 0 넣기
# 인접지점 방문 조건: 좌표내에 있고, 좌표==1, not visited
# 인접지점 방문처리, 큐에 넣기, 결과에 count += 1 넣기 
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[-1]*m for _ in range(n)] # -1: 방문안함, 0: 갈 수 없는땅
# result = [[-1]*m for _ in range(n)]

for i in range(n):
    inputList = list(map(int, sys.stdin.readline().split()))
    graph.append(inputList)

# 상하좌우
dir = [(-1,0), (1,0), (0,1), (0,-1)]
# bfs
def bfs(x, y):
    queue = deque()
    visited[x][y] = 0
    queue.append((x, y)) # 큐에 좌표, 거리 넣기

    while queue:
        cx, cy = queue.popleft() # 현재 좌표, 거리
        # result[cx][cy] = dist

        # 인접
        for (dx, dy) in dir:
            nx, ny = cx + dx, cy + dy
            if -1 < nx < n and -1 < ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            break

for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()

