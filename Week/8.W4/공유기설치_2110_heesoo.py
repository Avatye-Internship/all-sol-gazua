# 공유기설치
# 인터넷 참고해서 했음
import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()

# 공유기 서로 최대한 멀리 띄어놓기!!!!!!!

start, end = 1, arr[-1] - arr[0] # 거리 최소, 거리 최대
result = 0
while start<=end:
    mid = (start+end)//2 # 

    cnt = 1 # 1번에 공유기 놓고 시작 (최대거리는 1부터 맨끝 집일수있으니)
    prev = arr[0]
    for i in range(1,n):
        if arr[i] - prev >= mid: # 다음집과의 거리가 mid를 초과한다면 공유기 설치 가능!! 최대한 멀리 떨어트려야하니까
            cnt += 1
            prev = arr[i]
    
    if cnt >= c: # 공유기를 제한갯수 이상 설치했으면 공유기 사이 거리를 늘린다음에 다시 진행해봄
        result = max(result, mid)
        start = mid + 1
    else: 
        end = mid - 1

print(result)