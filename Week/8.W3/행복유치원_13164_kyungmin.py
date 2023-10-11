import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

array = []
for i in range(1, n):
    array.append(kids[i] - kids[i-1])

array.sort(reverse=True)
print(sum(array[k-1:]))

# 8명 중 4개의 그룹을 만든다고 할 때,
# 1  2  3  5  6  8  11 16  -> 오름차순으로 입력된 아이들의 키
#   1  1  2  1  2  3  5  -> 인접한 아이들 간의 키 차이

# => 키 차이를 내림차순 정렬
# 5 3 2 2 1 1 1
# 여기서 값이 큰 것 k-1개, 즉 3개를 빼주면 5 3 2가 제거된다.
# 따라서 인덱스가 3인 값부터 끝까지 sum을 구해주면 2+1+1+1=5 -> 티셔츠의 최소 비용