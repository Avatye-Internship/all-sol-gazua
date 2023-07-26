import math
#1212 8진수 2진수
# 8진수가 주어졌을때 2진수로 변환하는 프로그램 (n <= 30만..)
# 처음에 문자열에다 추가해주는 식으로 하니까 시간초과 -> 새로운 문자열 객체가 만들어지기 때문에 

n = input()
hexArr = ['000', '001', '010', '011', '100', '101', '110', '111']
results = []

for i in n:
    results.append(hexArr[int(i)])

results = ''.join(results)

if n == '0':
    print(0)
else:
    for i in results:
        if i != '0':
            print(results[results.index(i):])
            break
