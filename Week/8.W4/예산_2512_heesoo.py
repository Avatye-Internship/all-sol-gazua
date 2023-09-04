# 2512 예산
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr.sort()

start, end = 0, arr[-1]
result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    
    for i in arr:
        if i >= mid:
            total += mid
        else:
            total += i
    
    if total > m: # 총예산보다 크면
        end = mid - 1
    else:
        start = mid + 1

print(end)
