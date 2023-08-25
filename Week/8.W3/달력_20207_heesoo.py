# 20207 달력
import sys

# 2 4
# 4 5
# 5 6
# 5 7
# 7 9
# 11 12
# 12 12
# [0,1,1,2,3,1,2,1,1,0,1,2]

n = int(sys.stdin.readline())
arr = [0 for _ in range(367)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    for i in range(start, end+1):
        arr[i] += 1
        
width = 0
height = 0
total = 0
for i in range(1, len(arr)):
    if arr[i] > 0: # 일정 있다는 뜻
        width += 1
        height = max(arr[i], height)
    if arr[i] == 0: # 연속 일정 아니면 이전 연속 일정 저장해주고
        total += width*height
        width = 0
        height = 0

print(total)