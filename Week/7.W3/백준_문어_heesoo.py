# 21313 문어

# 문어 팔 8개
# 1. 서로 같은 번호의 손 잡기
# 2. 한 문어와 한 손만 잡기
# 3. 한손으로 여러 문어의 손잡기 불가능

# 인접한 두 문어가 잡은 손의 번호를 이용해 n 수열 만들기
# 사전순으로 제일 앞서는 수열 -> 1번 팔부터 손 잡기 시작
# 4개 쩍수 -> 1 2 1 2  
# 5개 홀수-> 1 2 1 2 -> x (3번 조건 위반)

# n <= 1000
n = int(input())

result = []

for i in range(n//2):
    result.append(1)
    result.append(2)
if (n%2 != 0):
    result.append(3)

for i in result:
    print(i, end=' ')

print(result)