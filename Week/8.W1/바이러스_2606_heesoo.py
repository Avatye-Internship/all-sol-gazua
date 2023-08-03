# 바이러스 2606
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 인접리스트 방식으로
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 방문 여부 초기화
visited = [False for _ in range(n+1)]

# BFS 함수 구현
def bfs(vertex):
    count = 0
    queue = deque([vertex])
    visited[vertex] = True

    while queue:
        currV = queue.popleft()
        count += 1

        for nextV in graph[currV]:
            if not visited[nextV]:
                queue.append(nextV)
                visited[nextV] = True

    return count

# 1번 컴퓨터에서 웜 바이러스에 걸리게 되는 컴퓨터 수 계산
result = bfs(1)
print(result-1)

