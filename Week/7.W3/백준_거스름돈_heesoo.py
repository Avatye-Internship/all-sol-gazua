# 14916 거스름돈

# 2원, 5원
# 동전의 개수가 최소가 되도록

# 1. 5원 가장 많이 나눌 수 있어야함

n = int(input()) # <= 100,000

result = 0
while n > 0 :
    # 남은 돈이 5로 나눠진다면 최소 -> break
    if (n % 5 == 0 ):
        result += n // 5
        break
    n -= 2 # 5로 안나눠지니까 2 빼본 다음에 다시 반복문 ㄱㄱ -> 다시 5로 나눠보게됨
    result += 1

if n < 0 :
    print(-1)
else :
    print(result)
       

