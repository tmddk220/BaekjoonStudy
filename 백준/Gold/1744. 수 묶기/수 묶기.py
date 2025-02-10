import sys
input = sys.stdin.readline

n = int(input())
old = [int(input()) for _ in range(n)]
    
plus = []
minus = []
new = []
zero = 0
for num in old:
    if num > 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    elif num == 1:
        new.append(num)
    else:
        zero = 1
        
plus.sort(reverse=True)
minus.sort()

if len(plus) % 2 == 0:
    for i in range(0, len(plus), 2):
        new.append(plus[i] * plus[i+1])
else:
    for i in range(0, len(plus)-1, 2):
        new.append(plus[i] * plus[i+1])
    new.append(plus[-1])
    
if len(minus) % 2 == 0:
    for i in range(0, len(minus), 2):
        new.append(minus[i] * minus[i+1])
else:
    for i in range(0, len(minus)-1, 2):
        new.append(minus[i] * minus[i+1])
    if zero == 0:
        new.append(minus[-1])

print(sum(new))