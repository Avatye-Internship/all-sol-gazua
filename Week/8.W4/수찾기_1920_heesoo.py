# 수찾기 1920
import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in arr:
    start, end = 0, n-1
    target = i

    while True:
        mid = (start+end)//2
        if start > end:
            print(0)
            break
        if target == A[mid]:
            print(1)
            break
        elif target < A[mid]:
            end = mid-1
        else:
            start = mid+1
