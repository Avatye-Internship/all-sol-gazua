import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# arr.sort()  #O(NlogN)

start, end = 1, max(arr)
result = 0
while start <= end: #O(log N)
    mid = (start+end)//2
    total = 0
    for h in arr: # O(N)
        if h >= mid:
            total += h - mid
    
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
