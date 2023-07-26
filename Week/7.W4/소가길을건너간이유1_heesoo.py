#14467 소가 길을 건너간 이유
# 소 위치 n번 관찰 -> 소가 최소 몇번 길을 건넜는지 = 같은 번호의 소가 위치를 몇번 바꿨는지
# 소 번호 : 1~10
# 소 위치 : 왼쪽 0 , 오른쪽 1
# 소가 길 건너간 최소 횟수

import sys
n = int(sys.stdin.readline())
cow = []
pos = []
count = 0

for i in range(n):
    currCow, currPos = map(int, input().split())
    # 이미 관찰된 소라면
    if currCow in cow:
        idx = cow.index(currCow)
        if pos[idx] != currPos: # 이전 소의 위치 vs 현재 소의 위치
            pos[idx] = currPos # 다르면 해당 소의 위치 새로 업데이트
            count += 1 # 이동횟수 추가
    # 처음 관찰된 소라면
    else:
        cow.append(currCow) # 소 번호, 위치 새로 추가
        pos.append(currPos)

print(count)
