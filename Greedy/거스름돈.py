import sys
input = sys.stdin.readline

money = int(input())
change_ls = [500, 100, 50, 10, 5, 1]
change = 1000 - money

ans = 0
for i in change_ls:
    while change >= i:
        change -= i
        ans += 1
        if change == 0:
            break

print(ans)