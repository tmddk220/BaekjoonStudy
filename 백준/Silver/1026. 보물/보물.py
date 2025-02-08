'''
리스트 a에서 제일 큰 값은 리스트 b에서 제일 작은 값과 매칭되어 계산되어야 한다.
즉, 정렬과 반복문을 통해 구현이 가능하다.
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
mn = 0

for i in range(n):
    mn += a[i] * b[i]
    
print(mn)