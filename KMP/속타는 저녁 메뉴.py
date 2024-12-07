# KMP
import sys
input = sys.stdin.readline

N = int(input())
T = list(map(str, input().split()))
P = list(map(str, input().split()))
P += P[:-1]


def compute_pi(p):
    m = len(p)
    pi = [0]*m

    j = 0
    for i in range(1, m):
        while p[i] != p[j] and j > 0:
            j = pi[j-1]

        if p[i] == p[j]:
            j += 1
            pi[i] = j

    return pi

pi = compute_pi(P)

ans = 0
n = len(P)
m = len(T)

i, j = 0, 0
while i < n:
    if P[i] == T[j]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = pi[j-1]

    if j == m:
        ans += 1
        j = pi[j-1]
    
for i in range(ans, 0, -1):
    if ans % i == 0 and N % i == 0:
        print(f"{ans//i}/{N//i}")
        break

