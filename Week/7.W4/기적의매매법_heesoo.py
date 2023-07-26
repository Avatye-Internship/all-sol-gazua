# 20546 기적의매매법
# BNP : 그때그때 살수있는만큼 다 삼
# TIMING : 
# 1. 3일 연속 가격이 상승하면 -> 샀던거 다 팔아버림
# 2. 3일 연속 가격이 하락하면 -> 다 사버림
import sys
bnp = timing = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

bnpCnt = 0
timingCnt = 0
# bnp
for i in range(14):
    cnt = bnp // arr[i]
    if cnt > 0 : # 몫이 크다는 것은 현재돈으로 살 수 있다는 뜻
        bnp -= cnt*arr[i] # 현재 돈에서 산만큼 빼기 
        bnpCnt += cnt # 매수한 주식 수 업데이트
bnp += bnpCnt*arr[13]

# timing
for i in range(3,13):
    # 상승
    if arr[i-3] < arr[i-2] < arr[i-1] < arr[i]:
        timing += arr[i]*timingCnt
    
    # 하락
    if arr[i-3] > arr[i-2] > arr[i-1] > arr[i]:
        cnt = timing // arr[i]
        if cnt > 0 : # 몫이 크다는 것은 현재돈으로 살 수 있다는 뜻
            timing -= cnt*arr[i] # 현재 돈에서 산만큼 빼기 
            timingCnt += cnt # 매수한 주식 수 업데이트
timing += timingCnt*arr[13]

if bnp == timing:
    print('SAMESAME')
elif bnp > timing:
    print('BNP')
else:
    print('TIMING')
