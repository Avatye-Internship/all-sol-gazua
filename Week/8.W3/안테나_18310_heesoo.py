# 18310 안테나
# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록, 집이 위치한 곳에만 설치 가능
# O(N)으로 풀어야함 -> 각 집마다 거리 검사하는 방법 안됨(O(N^2))
# 중간값기준으로
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
mid = (n-1)//2
print(arr[mid])

# 평균값 안되는 이유: 

