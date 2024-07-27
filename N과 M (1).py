import sys

n, m = map(int, sys.stdin.readline().split())

ls = []
def btc():
    if len(ls) == m:
        print(*ls)
        return
    for i in range(1, n+1):
        if i not in ls:
            ls.append(i)
            btc()
            ls.pop()
btc()