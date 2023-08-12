# 2667 단지번호 붙이기
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
visited = [[False]*n for _ in range(n)]
result = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# 1. 시작노드 : 그래프 = 1, 방문x
# 2. 시작노드 방문처리 + 큐에 넣기
# 3. while문 들어감
# 3. 상하좌우중에 방문x, == 1인곳 방문처리 + 큐에 넣기
# 4. 큐에

# 상하좌우
dir = [(-1,0), (1,0), (0,1), (0,-1)]
# bfs
def bfs(x, y):
    count = 1
    queue = deque()
    visited[x][y] = True
    queue.append((x, y)) # 큐에 좌표를 저장

    while queue:
        cx, cy = queue.popleft() # 현재 좌표

        # 인접
        for (dx, dy) in dir:
            nx, ny = cx + dx, cy + dy
            if -1 < nx < n and -1 < ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            # 거기부터 시작
            howmany = bfs(i, j)
            result.append(howmany)

result.sort()

print(len(result))
for r in result:
    print(r)