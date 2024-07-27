# backtracking!!

N, S = map(int, input().split())

ls = list(map(int, input().split()))
ls_sum = []
cnt = 0

def btc(start=0):
    global cnt

    if sum(ls_sum) == S and len(ls_sum) > 0:
        cnt += 1       

    for i in range(start, N):
        ls_sum.append(ls[i])
        btc(i + 1)
        ls_sum.pop()

btc()
print(cnt)

''' no backtracking

N, S = map(int, input().split())

ls = list(map(int, input().split()))
cnt = 0

sum_ls = [[]]
for i in ls:
    for j in range(len(sum_ls)):
        sum_ls.append(sum_ls[j] + [i])

for k in range(1, len(sum_ls)):
    if sum(sum_ls[k]) == S:
        cnt += 1

print(cnt)

'''