# 14916 거스름돈
import sys
money = int(sys.stdin.readline())
count = -1
# money가 1보다 크고 3이 아닐 경우
if(money > 1 and money!= 3):
    # 5로 나누어 떨어지는가
    if(money % 5 == 0):
        count = money //5
    else:
        count = (money // 5)
        # 5로 나눈 잔액이 짝수인가
        if((money%5)%2 != 0):
            count -=1 # 짝수 아닐경우 count-1
        money -= count *5
        count += money //2
print(count)