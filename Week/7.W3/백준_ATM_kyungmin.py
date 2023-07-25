# 11399 ATM

n = int(input())
peoples = list(map(int, input().split()))  # 기다리는 사람들을 리스트 형태로 입력 받는다

peoples.sort()  # 작은 순서대로 정렬
answer = 0  # 정답 변수를 0

for x in range(1, n+1):
    answer += sum(peoples[0:x])  # 리스트의 0번째 수부터 x번째 수까지를 더해줌
print(answer) 