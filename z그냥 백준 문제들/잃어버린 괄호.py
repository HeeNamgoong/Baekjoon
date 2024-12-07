import sys
input = sys.stdin.readline

num = input().split('-')
num[-1] = num[-1].rstrip('\n')

ls = []
for i in num:
    i = i.split('+')
    for j in range(len(i)):
        i[j] = int(i[j])
    ls.append(sum(i))

ans = ls[0]
for k in range(len(ls)-1):
    ans = ans - ls[k+1]
print(ans)