import sys

N, K = map(int, sys.stdin.readline().split())

WV = []
for i in range(N):
    # W, V
    WV.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


max_ans = 0
for i in range(1, N+1):
    for j in range(1, K+1):
        if WV[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(WV[i-1][1] + dp[i-1][j-WV[i-1][0]], dp[i-1][j])


        # max_ans = max(dp[i][j], max_ans)
        max_ans = dp[i][j]


print(max_ans)





# 함수 버전 - 시간 더 빠름
'''
import sys

def knapsack(N, K):

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    max_ans = 0

    for i in range(1, N+1):
        for j in range(1, K+1):
            if WV[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(WV[i-1][1] + dp[i-1][j-WV[i-1][0]], dp[i-1][j])


            # max_ans = max(dp[i][j], max_ans)
            max_ans = dp[i][j]


    return max_ans
    
N, K = map(int, sys.stdin.readline().split())

WV = []
for i in range(N):
    # W, V
    WV.append(list(map(int, sys.stdin.readline().split())))


ans = knapsack(N, K)

print(ans)
'''