# 11724 연결요소의 개수
# 방향 없는 그래프가 주어졌을때 연결요소의 개수 구하는 프로그램
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(currV):
    # 현재 노드 방문처리
    visited[currV] = True
    # 인접노드 확인
    for near in graph[currV]:
        # 방문하지 않은 곳이면
        if not visited[near]:
            # 그곳에서 다시 돌기
            dfs(near)

# 여러곳에서 출발
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
