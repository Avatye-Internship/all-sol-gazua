# 2644 촌수계산 -> 전부 탐색해야함으로 DFS 사용
import sys

n = int(input()) #사람 수
p1, p2 = map(int, input().split()) # 촌수 계산 사람 2명
m = int(input()) # 반복 수

graph = {} # 딕셔너리로 저장
visited = [False] * (n+1) # 노드 방문여부
for i in range(m):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x]=[y] #배열로 value 저장하기
    else:
        graph[x].append(y)
    if y not in graph.keys():
        graph[y]=[x] #배열로 value 저장하기
    else:
        graph[y].append(x)

def DFS(start,end,visited):
    visited[start] = True

    if start == end: # start, end 같으면 0
        return 0
    
    for i in graph[start]:
        if not visited[i]:
            count = DFS(i,end,visited) # DFS 함수의 return 값으로 촌수 계산
            if count != -1:
                return count+1
        
    return -1 #촌수 못 찾은 경우

result = DFS(p1,p2,visited)
print(result)