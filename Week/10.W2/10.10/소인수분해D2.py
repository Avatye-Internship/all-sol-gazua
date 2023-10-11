import sys

N = int(input())

def sol(n):
    d=2
    while d <= n :
        if(n%d == 0):
            # print(d)
            if(d==2):arr[0]+=1
            elif(d==3):arr[1]+=1
            elif(d==5):arr[2]+=1
            elif(d==7):arr[3]+=1
            elif(d==11):arr[4]+=1
            n = n/d
        else:
            d+=1

for i in range(N):
    num = int(input())
    arr = [0]*5
    sol(num)
    print("#",end="")
    print(i+1,*arr)
