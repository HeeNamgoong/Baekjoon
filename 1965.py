import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(1, i+1):
        if num[j-1] < num[i]:
            dp[i] = max(dp[i], dp[j-1] + 1)

print(max(dp))