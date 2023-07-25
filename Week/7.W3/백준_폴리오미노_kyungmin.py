# 1343 폴리오미노

# 처음에 'X' , '.'으로 이루어진 보드판이 주어졌을 때, 민식이는 가능한 AAAA와 BB로 채워 사전 순으로 가장 앞서는 답을 출력한다. 만약 모두 덮을 수 없으면 -1을 출력

board = input() # 문자열 입력받기
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
 
if 'X' in board:
    print(-1)
else:
    print(board)