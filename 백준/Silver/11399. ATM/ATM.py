'''
입력값이 n = 5, p = [3, 1, 4, 3, 2]일 때 결과값은 32이다.
문제에서 제시한 것처럼, 시간의 합을 최소로 하려면 리스트 p의 원소가 오름차순으로 정렬된 상태여야 한다.
리스트 p가 오름차순으로 정렬되었다는 가정하에 결과값이 구해지는 과정을 분석하면 아래와 같다.
answer = (p[0] * n) + (p[1] * (n-1)) + (p[2] * (n-2)) + (p[3] * (n-3)) + (p[4] * (n-4))
반복문을 활용해서 효율적으로 answer을 구할 수 있다.
'''

n = int(input())
p = list(map(int, input().split()))
p.sort()

answer = 0

for i in range(n):
    answer += p[i] * (n-i)

print(answer)