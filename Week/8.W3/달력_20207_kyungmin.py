import numpy as np
from collections import Counter

N = int(input())
calendar =[]

total = 0

for i in range(N):
    start,end = map(int, input().split())
    calendar.append([start,end])

#시작일,긴것 기준으로 정렬
# - 붙이면 reverse=True
calendar.sort(key=lambda x: (x[0],x[1]))
cnt=[0 for _ in range(calendar[N-1][1]+1)]

#처음 시작 지정
startDate = calendar[0][0]
endDate = calendar[0][1]

for cal in calendar:
    print(calendar.index(cal))
    if(cal[0] > endDate or calendar.index(cal) == N-1):
        arr = cnt[startDate:endDate]
        total += ((endDate-startDate)+1) * max(arr)

    if(startDate <= cal[0] <= endDate and endDate < cal[1]):
        endDate = cal[1]
    else:
        startDate = cal[0]
        endDate = cal[1]

    for i in range(cal[0],cal[1]+1):
        cnt[i] +=1


print(total)