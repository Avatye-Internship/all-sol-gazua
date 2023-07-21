# 2875 대회 or 인턴
import sys

input_line = sys.stdin.readline().strip()
input_list = input_line.split()
int_list = list(map(int, input_list))
N, M, K = int_list[0], int_list[1], int_list[2]
# 남, 여 각각의 팀 cnt
w_cnt = N//2
m_cnt = M
person =1
max_cnt = max(w_cnt,m_cnt)
min_cnt = min(w_cnt,m_cnt)
result = 0
if(w_cnt > m_cnt):
    person = 2
# ( max_cnt - min_cnt ) * person 이 인턴 인원수보다 크거나 같은경우
if((max_cnt-min_cnt)*person >= K):
    result = min_cnt
else:
    K -= (max_cnt-min_cnt)*person
    # 3의 배수인 경우
    if(K%3 ==0):
        result = min_cnt - (K//3)
        # 3의 배수가 아닌경우
    else:
        result = min_cnt - (K//3 + 1)

print(result)


