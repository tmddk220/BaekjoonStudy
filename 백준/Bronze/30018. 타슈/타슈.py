n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = []
answer = 0

for i in range(len(a)):
    tmp.append(int(b[i]-a[i]))

for i in tmp:
    if i > 0:
        answer += i
print(answer)