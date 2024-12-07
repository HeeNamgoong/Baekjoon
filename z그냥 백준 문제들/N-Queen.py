N = int(input())

ls = []
cnt = 0

def btc():
    if cnt == N:
        cnt += 1 
        return
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if [i, j] not in ls:
                ls.append(i)
                btc()
                ls.pop()
    # cnt = 0

    