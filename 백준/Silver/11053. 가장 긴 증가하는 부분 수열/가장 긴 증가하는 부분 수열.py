import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))