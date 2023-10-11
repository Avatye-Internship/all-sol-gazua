import sys
#numPy import 해서 런타임에러남
# 문제 잘못 이해함
# -> 그 다음날도 이어지는 줄 모르고 겹쳐야지만 이어진다고 생각

N = int(input())
calendar =[]
max_end_day =0
total = 0

for i in range(N):
    start,end = map(int, input().split())
    if end > max_end_day : 
        max_end_day = end
    calendar.append([start,end])

#시작일,긴것 기준으로 정렬
# - 붙이면 reverse=True
calendar.sort(key=lambda x: (x[0],x[1]))

cnt = [0] * (max_end_day + 1)

#처음 시작 지정
startDate = calendar[0][0]
endDate = calendar[0][1]

for i,cal in enumerate(calendar):
    for j in range(cal[0],cal[1]+1):
        cnt[j] +=1
    
    if(cal[0] > endDate+1):
        max_day = max(cnt[startDate:endDate+1])
        total += ((endDate-startDate)+1) * max_day

    if(startDate <= cal[0] <= endDate+1):
        if endDate < cal[1]:
            endDate = cal[1]
    else:
        startDate = cal[0]
        endDate = cal[1]
    
    if(i == N-1):
        max_day = max(cnt[startDate:endDate+1])
        total += ((endDate-startDate)+1) * max_day

print(total)
    


# 런타임 에러 나는 이유 

# 1. 배열에 할당된 크기를 넘어서 접근했을 때
# 2. 전역 배열의 크기가 메모리 제한을 초과할 때
# 3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
# 4. 0으로 나눌 떄
# 5. 라이브러리에서 예외를 발생시켰을 때
# 6. 재귀 호출이 너무 깊어질 때
# 7. 이미 해제된 메모리를 또 참조할 때