#팰린드롬만들기_1213

Hansoo_name = input()
# 알파벳 순서별 정렬
sort_name = sorted(Hansoo_name)
dic ={}
odd_count = 0
result =[]
# 딕셔너리에 저장
for c in sort_name:
    if c in dic:
        dic[c] +=1
    else:
        dic[c] =1

# 홀수 개수인 알파벳의 개수 저장
odd = [k for k, v in dic.items() if v %2 != 0]

#이름의 길이가 짝수이고 알파벳들의 개수가 모두 짝수일때
if(len(Hansoo_name)%2==0 and len(odd) == 0):
    for i in dic.keys():
        for j in range(dic[i]//2):
            result.append(i)
    
    #반대로 다시 출력
    for i in range(len(result),0,-1):
        result.append(result[i-1])
    print(*result,sep='')
# 이름의 길이가 홀수이고 알파벳들의 개수 중 홀수가 1개 일때
elif(len(Hansoo_name)%2!=0 and len(odd) == 1):
    for i in dic.keys():
        # 짝수이거나 홀수인데 개수가 1 초과일때
        if dic[i]%2==0 or dic[i] > 1:
            for j in range(dic[i]//2):
                result.append(i)
    # 홀수 출력
    result.append(odd[0])

    # 반대로 다시 출력
    for i in range(len(result)-1,0,-1):
        result.append(result[i-1])
    print(*result,sep='')
else:
    print("I'm Sorry Hansoo")
