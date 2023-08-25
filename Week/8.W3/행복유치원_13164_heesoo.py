# 13164 행복유치원
import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# 비용 : 가장 키가 큰 원생 - 키 작은 원생 1 3 5 6 10

price = 0
diff = [arr[i]-arr[i-1] for i in range(1,n)]
diff.sort(reverse=True)

result = sum(diff[k-1:])
print(result)
