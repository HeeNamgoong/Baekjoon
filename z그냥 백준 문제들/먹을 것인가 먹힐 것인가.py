# 시간 초과
'''
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = 0

    for p in range(N):
        for q in range(M):
            if A[p] > B[q]:
                ans += 1
    print(ans)
'''

# solution - 이진 탐색

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    
    ans = 0
    b = 0

    for a in A:
        while b < M:
            if a > B[b]:
                b += 1
            else:
                break
        ans += b
    print(ans)

