# 틀림 - 1 4 2 3 <- 이런 반례에서 반함
'''
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

max_len = 0
ls_ = [seq[0]]
ans = []

for i in range(N-1):
    for j in range(i+1, N):
        if ls_[max_len] < seq[j]:
            ls_.append(seq[j])
            max_len += 1
    ans.append(max_len)
    ls_ = [seq[i+1]]
    max_len = 0

print(max(ans) + 1)
'''




# import sys
# input = sys.stdin.readline

# N = int(input())
# seq = list(map(int, input().split()))


# ls_ = [seq[0]]
# ans = []

# for i in range(1, N):
#     if ls_[-1] < seq[i]:
#         ls_.append(seq[i])
#     ls_ = [seq[i+1]]

# print(max(ans) + 1)


import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))