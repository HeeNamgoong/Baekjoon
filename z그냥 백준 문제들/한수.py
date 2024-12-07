N = int(input())
cnt = 0

if N < 100:
    print(N)
else:
    for num in range(100, N+1):
        num_ls = []
        num_ls += str(num)
        if int(num_ls[0]) - int(num_ls[1]) == int(num_ls[1]) - int(num_ls[2]):
            cnt += 1
    print(99 + cnt)