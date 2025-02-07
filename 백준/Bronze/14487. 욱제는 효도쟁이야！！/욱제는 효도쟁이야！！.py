'''
문제의 입출력값들을 살펴보면 쉽게 힌트를 얻을 수 있다.
힌트는 바로 리스트 v에서 가장 큰 값을 제외하고 나머지 원소들의 합을 구하는 것.
n = 5, v = [1, 6, 5, 2, 4]일 때, 가장 큰 값인 6을 제외하고 1+5+2+4를 수행하면 결과값은 12가 나온다.
'''

n = int(input())
v = list(map(int, input().split()))
v.sort()
v.pop()

answer = sum(v)
print(answer)