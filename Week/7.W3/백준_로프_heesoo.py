# 2217 로프

# k개 로프를 사용해 w 물체 들어올릴때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량 걸림
# 들어올릴 수 있는 물체의 최대 중량

n = int(input())
weight = []
for i in range(n):
    temp = int(input())
    weight.append(temp)

weight.sort(reverse=True) # 무거운 순서로 정렬

lope = 1 # 현재 로프 개수
maxW = weight[0] # 현재 최대 무게

for i in weight[1:]:
    lope += 1
    maxW = max(maxW, i*lope)

print(maxW)