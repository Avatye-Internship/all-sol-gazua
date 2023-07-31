# 2217 로프

n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))
k.sort() #정렬

answers = []
for x in k: 
    answers.append(x*n) #제일 작은 로프부터 최대값 넣기
    n -= 1 
print(max(answers)) # 제일 큰 값