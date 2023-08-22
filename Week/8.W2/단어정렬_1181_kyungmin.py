import sys

N = int(input()) # 반복 수
words=[]
print_words=[]

for i in range(N):
    word = input()
    if word not in words:
        words.append(word)

#words.sort(key = lambda(x: x[1],x[2]))
# 순서를 지켜야하는경우, set말고 for문 사용하기
print_words = sorted(words,key=lambda x: (len(x),x))

for i in print_words:
    print(i)