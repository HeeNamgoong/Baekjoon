# KMP
import sys
input = sys.stdin.readline

L = int(input())
str = input().rstrip()

def compute_pi(p):
    m = len(p)
    pi = [0] * m
    i = 1
    j = 0

    while i < m:
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            i += 1
        elif j == 0:
            pi[i] = j
            i += 1
        else:
            j = pi[j-1]
    return pi

pi = compute_pi(str)
print(L - pi[-1]) # 광고판의 크기 - 공통되는 가장 긴 부분