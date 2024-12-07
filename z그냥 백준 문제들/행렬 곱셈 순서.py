import sys
input = sys.stdin.readline

N = int(input())
matrix = []

for i in range(N):
    r, c = map(int, input().split())
    matrix.append((r,c))

def foo(p):
    n = len(p)
    dp = [[-1] * n for _ in range(n)]

    def S(s, e):
        pass