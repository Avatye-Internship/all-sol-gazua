# 21313 문어
import sys
N = int(sys.stdin.readline())
sequence = [1, 2] * (N // 2)
for num in sequence:
    print(num, end=' ')
# 짝수인 경우 -> N/2 만큼 1 2 반복
if N % 2 == 0:
    print()
# 홀수인 경우 -> N/2 만큼 1 2 반복 + 3
else :
    print('3')