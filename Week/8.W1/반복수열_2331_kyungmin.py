# 2331 반복수열
import sys
import math
A, P = map(int, input().split())
num = [A]
while True:
    digits = list(map(int, str(A)))
    result = sum(digit ** P for digit in digits)
    if result not in num:
        num.append(result)
    else:
        break
print(num)

def sum(A):
    digits = list(map(int, str(A)))
    result = sum(digit ** P for digit in digits)