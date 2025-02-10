import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

count = 0

for i in range(n-2, -1, -1):
    if nums[i] >= nums[i+1]:
        count += nums[i] - (nums[i+1]-1) 
        nums[i] = nums[i+1] - 1

print(count)