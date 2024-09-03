import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# k = 0
# for i in range(N):
#     while (k != M):
#         B.insert(i+1, C[k])

#         if A[i] == 0: # 큐
#             ans = B[i+1]
#             del B[i+1]
#         else: # 스택
#             ans = B[i+2]
#             del B[i+2]
#         k += 1
#     print(ans)


k = 0
i = 0
while (k != M):
    B.insert(i+1, C[k])

    if A[i] == 0: # 큐
        ans = B[i+1]
        del B[i+1]
    else: # 스택
        ans = B[i+2]
        del B[i+2]
    k += 1
print(ans)