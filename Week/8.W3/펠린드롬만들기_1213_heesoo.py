# 1213 거꾸로 읽어도 똑같은 문자 만들기
import sys
from collections import Counter
# 홀수개수인게 2개 이상이면 break
# 모두 짝수면 ok
name = sys.stdin.readline().rstrip()
name = sorted(list(name))
nameArr = {}
oddCount = 0
for i in name:
    if i not in nameArr.keys():
        nameArr[i] = 1
    else:
        nameArr[i] += 1

for k, v in nameArr.items():
    if v % 2 != 0:
        oddCount += 1

if oddCount >= 2:
    print("I'm Sorry Hansoo")
else:
    str = ''
    oneodd = ''
    for k, v in nameArr.items():
        # 짝수면 넣기
        if v % 2 == 0:
            str += k*(v // 2)
        # 홀수면
        else:
            if v == 1: # 마지막에 넣어야함
                oneodd = k
            else:
                str += k*(v//2)
                oneodd = k
    
    if oneodd != '':
        print(str+oneodd+str[::-1])
    else:
        print(str+str[::-1])


