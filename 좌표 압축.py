import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

set_num = set(num)
set_num = sorted(set_num)

dict_num = {}
for i in range(len(set_num)):
    dict_num[set_num[i]] = i

for i in range(N):
    print(dict_num[num[i]], end=' ')