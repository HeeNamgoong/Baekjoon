import sys
input = sys.stdin.readline

S = int(input())

n = 1
while True:
    if n*(n+1)/2 >= S:
        break
    n += 1


if n*(n+1)/2 - S > 0:
    print(n-1)
elif n*(n+1)/2 - S == 0:
    print(n)