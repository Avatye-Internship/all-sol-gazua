N = int(input())
# 소별로 이동 횟수
countArr = [0] * 10
# 소 위치
cowArr = [0] * 10

for i in range(N) :
    cow, location = map(int,input().split())
    # 처음 위치인 경우
    if(countArr[cow-1]==0):
        cowArr[cow-1] = location
        countArr[cow-1] +=1
    # 또 다시 관찰된 경우
    else:
        # 소가 이동한 경우
        if(cowArr[cow-1] != location):
            countArr[cow-1] +=1
            cowArr[cow-1] = location
# 처음 위치에 +1을 해서 빼줌
for i in range(10) : 
    if(countArr[i]>0):
        countArr[i] -=1

print(sum(countArr))
    