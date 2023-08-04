# 2331 반복수열
import sys
A, P = map(int, sys.stdin.readline().split())
arr = []
arr.append(A)
idx = 0
while True:
    count = 0
    for i in str(arr[idx]):
        count += int(i)**P 

    if count in arr:
        print(len(arr[:arr.index(count)]))
        break
    else:
        arr.append(count)
        idx += 1
