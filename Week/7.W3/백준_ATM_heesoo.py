# 11399 ATM

# 모두 돈을 인출하는데에 걸리는 최소 시간
# 가장 앞에 서있는 사람이 빨리 인출해야됨

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split())) # 인출하는데에 걸리는 시간

p.sort() # 가장 짧게 걸리는 순서대로 정렬
result = []
result.append(p[0])
ans = p[0]
for i in range(1,n):
    result.append(result[i-1] + p[i]) # 이전 사람 걸린시간 + 본인 걸린시간

print(sum(result))


