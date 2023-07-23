# 1343 폴리오미노

# X만 모두 폴리오미노(AAAA, BB)로 덮기
# 일단 . 기준으로 나누고 4개, 2개로 나눠 떨어지지않는 것들 -1
# 4, 2로 나눠지는것인지 검사 기준 : 짝수
# 사전순으로 출력해야되니까 A먼저

board = input()

board = board.replace('XXXX', 'AAAA') # XXXX 연속되어있는거 AAAA로 먼저 바꿈
board = board.replace('XX', 'BB') # 다음에 XX가 남아있으면 BB로 바꿔줌

if 'X' in board: # 아직 X가 남아있다면 바꿀 수 없었다는 것
    print(-1)
else:
    print(board)





# ------------위에 답 이전 풀이------------
board = input()

result = ""
idx = 0

while idx < len(board):
    # X로 시작하는지 검사
    if board[idx] == 'X':
        # 남은 X가 2개인지 검사
        if len(board[idx:]) == 2:
            result += 'BB'
            idx += 2
        # 남은 연속된 X가 4개 이상이면 AAAA로 바꾸기 
        elif len(board[idx:]) >= 4 and board[idx:idx+4] == 'XXXX':
            result += 'AAAA'
            idx += 4
        else:
            # 위의 두가지 경우가 아니라면 연속된 짝수개의 X가 없다는것
            result = -1
            break
    else:
        # . 도 추가
        result += board[idx]
        idx += 1

print(result)


