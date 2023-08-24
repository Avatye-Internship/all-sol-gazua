#5547 일루미네이션
# /////// 
# \\\\\\\
# 0 1 0 1 0 1 1 1
# 0 1 1 0 0 1 0 0
# 1 0 1 0 1 1 1 1
# 0 1 1 0 1 0 1 0
import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())
graph = []
# 첫 번째 행 추가 (0으로 채움)
graph.append([0] * (w + 1))
for i in range(h):
    inputList = [0] + list(map(int, sys.stdin.readline().split()))
    graph.append(inputList)

# 주변이 범위밖 or 0 -> 벽 += 2
dir = [(-1,0), (1,0), ()]
def bfs(x, y):
    queue = deque()
    while queue:
        queue.popleft()
        # 홀수면 들러야할곳
        dir = [(-1,0), (1,0), (0,-1),(0,1)]
        for 

for y in range(h):
    for x in range(w):
        # 짝수
        if y%2 == 0:
            pass
        else :
            pass
        if graph[x][y] == 1:
            bfs()