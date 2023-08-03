# 1260 DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과 출력
# 방문할 정점 여러개면 번호가 작은것 먼저 방문
import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

dfsResult = []
bfsResult = []
# 인접리스트 방식으로
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
for list in graph:
    list.sort()

def dfs(vertex):
    
    # 현재 노드(vertex)와 인접한 노드(currV)중에
    for currV in graph[vertex]:
        # 아직 방문하지 않은 노드가 있다면
        if not visited[currV]:
            print(currV, end=' ') # 현재 노드 빼내기
            visited[currV] = True # 방문처리
            dfs(currV) # 그 노드부터 다시 탐색

print(v, end=' ')
visited[v] = True
dfs(v)
print()
visited = [False for _ in range(n+1)]

from collections import deque

q = deque()
            
def bfs():
    while q:
        # 현재 큐에 있는것 pop
        currV = q.popleft()
        # 현재 노드와 인접한 노드 다 방문처리
        for nextV in graph[currV]:
            if not visited[nextV]:
                print(nextV, end=' ')
                visited[nextV] = True
                q.append(nextV)

print(v, end=' ')
visited[v] = True
q.append(v)
bfs()
