import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 2

def fibo(n):
    if dp[n] == 0:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

fibo(n)

print(dp[n-1] % 10007)


