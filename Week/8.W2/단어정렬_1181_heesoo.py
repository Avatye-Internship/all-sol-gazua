# 1181 실버5
import sys

n = int(sys.stdin.readline()) # n <= 20000
word = []

for i in range(n):
    temp = sys.stdin.readline()
    if temp not in word:
        word.append(temp)

word.sort() # 2순위: 사전순
word.sort(key= len) # 1순위: 길이순

for i in range(len(word)):
    print(word[i])