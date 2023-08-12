# 16918 봄버맨
# 폭탄 -> 3초 후 폭발 -> 폭탄칸 빈칸 + 인접 네칸 빈칸, 인접한칸에 폭탄 있는 경우 폭발없이 그냥 파괴됨
# 구현해야할기능
# 1. 폭탄있는곳 위치 큐에 넣기
# 2. 모든 좌표 폭탄으로 채우기
# 3. 3초전에 만들어진 폭탄 터트리기

# 1초 : bombPosSave (큐 : 1초꺼만 들어가있음)
# 2초 : fullbomb (큐 : 변화없음)
# 3초 : bomb (큐 : 1초 위치에 있던 애들만 터짐)
#    : bombPosSave (큐 : 터트리고 살아남은 폭탄 위치 저장 = 2초에 생긴 애들)
# 4초 : fullbomb (큐 : 변화없음)
# 5초 : bomb ()
 
import sys
from collections import deque

r, c, n = map(int, sys.stdin.readline().split())
graph = [] 
# 상하좌우
dir = [(-1,0), (1,0), (0,1), (0,-1)]

for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

queue = deque()

# 폭탄 위치 저장
def bombPosSave():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O': # 폭탄 있는 위치 큐에 넣기
                queue.append((i, j))

def fullBomb():
    for i in range(r):
        for j in range(c):
            graph[i][j] = 'O'

def bomb():
    while queue:
        cx, cy = queue.popleft()
        # 폭탄 본인 터트리기
        graph[cx][cy] = '.' 
        # 상하좌우 터트리기
        for (dx, dy) in dir:
            nx, ny = cx + dx, cy + dy
            if -1 < nx < r and -1 < ny < c:
                graph[nx][ny] = '.'

# 초기(time=1) 상태 저장
for time in range(1, n+1):
    if time == 1:
        bombPosSave()
    elif time%2 == 0:
        fullBomb()
    else:
        bomb()
        bombPosSave()

for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()
