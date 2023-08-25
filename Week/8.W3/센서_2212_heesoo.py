# 2212 센서 O(N2)
# 집중국을 어디다 놔야지 짧은거리에 많
# 최대 k개 집중국의 수신 가능 영역 길이의 합의 최솟값
# 1, 3, 6, 6, 7, 9
#   2, 3, 0, 1, 2
# 3에 하나 놓고, 7에 하나 놓고 -> 2 + 3
# 3, 6, 7, 8, 10, 12, 14, 15, 18, 20
# 중간값 기준으로 최소 거리 = end-start // 2 
# 거기서 짝수면 그 반 나눈걸 다시 반으로 나눠서
# k=1 중간값(n//2) +- dist 커버가능한가 확인
# k=2 n//2//2 +- dist//2
# 2212 센서
# 그리디
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

dist = [arr[i]-arr[i-1] for i in range(1,n)]
dist.sort(reverse=True)
result = sum(dist[k-1:])
print(result)

