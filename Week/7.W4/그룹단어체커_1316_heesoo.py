# 1316 그룹단어체커
# 그룹단어 : 각 문자가 연속해서 나타나는 경우
# 연속 검사 : 바로전 값과 같으면 continue, 
#           바로전 값과 다른데 이전에도 등장하는거라면 break
#           바로전 값과 다른데 처음 등장하는거라면 배열에 넣어주기

import sys
N = int(sys.stdin.readline())
result = 0
for i in range(N):
    temp = []
    word = sys.stdin.readline()
    
    temp.append(word[0]) # 맨 첫번째값 넣어주고 시작
    flag = True # 연속단어 여부
    for k in range(1, len(word)):
        if word[k] == word[k-1]: # 바로 전 값과 같으면 연속oo
            continue
        else:
            if word[k] in temp: # 이 전에 등장했던 값
                flag = False
                break
            else: # 처음 등장하는 값
                temp.append(word[k])

    if flag: result += 1

print(result)
    

