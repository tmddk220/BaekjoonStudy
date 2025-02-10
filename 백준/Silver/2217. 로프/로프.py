import sys
input = sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    data.append(int(input()))
    
data.sort()

answers=[]
for i in data:
    answers.append(i*n)
    n -= 1
    
print(max(answers))