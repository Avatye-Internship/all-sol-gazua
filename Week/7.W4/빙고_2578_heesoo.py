# 2578 빙고
# 몇번째에 빙고가 되는지
# 빙고 : 3개
import sys
board = [[0]*5 for _ in range(5)]
check = [[0]*5 for _ in range(5)]
num = []
result = 0

def isBingo(i, j):
    # 가로열 검사
    count = 0
    if check[i].count(1) == 5:
        count += 1
    # 세로열 검사
    if check[0][j]+check[1][j]+check[2][j]+check[3][j]+check[4][j] == 5:
        count += 1
    # 왼쪽대각선 검사
    if i == j:
        if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5: count += 1
    # 오른쪽대각선 검사
    if i+j == 4:
        if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5: count += 1    
    
    return count

for i in range(5):
    board[i] = list(map(int, sys.stdin.readline().split()))

for i in range(5):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp:
        num.append(j)

for i in range(25):
    for rowIdx, rowArr in enumerate(board):
        if num[i] in rowArr:
            colIdx = rowArr.index(num[i])
            check[rowIdx][colIdx] = True
            break
    result += isBingo(rowIdx, colIdx)

    if result >= 3:
        print(i+1)
        break



