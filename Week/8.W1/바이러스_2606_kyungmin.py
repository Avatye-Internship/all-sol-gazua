# 바이러스 2606
N = int(input()) # 노드 개수
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    # 인접 노드 추가
    graph[a].append(b)
    graph[b].append(a)
# 방문 여부
visited = [False] * (N+1)
count = -1

def DFS(v):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(1)
print(count)