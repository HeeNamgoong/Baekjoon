ls = []
for i in range(9):
    height = int(input())
    ls.append(height)

ls_sum = []
ans = []
cnt = 0

def btc(start=0):
    global cnt

    if len(ls_sum) == 7 and sum(ls_sum) == 100:
        cnt += 1
        ls_sum.sort()
        if cnt == 1:
            for i in ls_sum:
                print(i)
    
    for i in range(start, 9):
        ls_sum.append(ls[i])
        btc(i + 1)
        ls_sum.pop()

btc()


