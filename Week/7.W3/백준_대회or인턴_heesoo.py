# 2875 대회 or 인턴

# 1팀 : 여학생 2명, 남학생 1명
# 만들 수 있는 최대의 팀 수

n, m, k = map(int, input().split())

people = n+m-k # 참가 가능 인원
team = people // 3 # 만들 수 있는 최대 팀
cnt = 0 # 현재 만든 팀

for i in range(team): # 만들 수 있는 최대 팀 개수 만큼 반복
    if (n-2 >= 0 and m-1 >= 0): # 여자2명 남자1명 팀에 넣어지면 팀 개수 + 1
            cnt += 1
            n -= 2  
            m -= 1 
    else:
        break

print (cnt)

# -> greedy인 이유?



