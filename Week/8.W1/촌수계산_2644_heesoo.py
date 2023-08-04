# 2644 촌수계산

import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[]*(n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = []

for i in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)  
    graph[child].append(parent) 

# dfs -> 촌수계산해야하기 때문에 그래프를 간선의 길이가 1인것으로 설정하고 둘중에 하나의 노드에서 시작해서 가려구
def dfs(curr, depth):
    if curr == b:
        result.append(depth)
        return 
    visited[curr] = True
    for near in graph[curr]:
        if not visited[near]:
            dfs(near, depth + 1)

dfs(a, 0)

if len(result) == 0:  # 만약 a에서 b까지 도달할 수 없다면 -1 출력
    print(-1)
else:
    print(result[0])