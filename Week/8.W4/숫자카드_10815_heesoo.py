# 숫자카드
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

card.sort() # sort 몇만까지?

# 재귀함수 방법
def binarySearch(target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if target == card[mid]:
        return mid
    elif target < card[mid]:
        return binarySearch(target, start, mid-1)
    else:
        return binarySearch(target, mid+1, end)

# O(N) 
for i in arr:
    result = binarySearch(i, 0, n-1)
    if result == None:
        print(0, end=' ')
    else:
        print(1, end=' ')
