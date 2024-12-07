''' 메모리 초과
N = int(input())

check = [1] * N

for i in range(2, N+1):
    for j in range(1, N+1):
        while i*j <= N:
            if (i*j) % i == 0:
                if check[i*j - 1] == 0:
                    check[i*j - 1] = 1
                    break
                elif check[i*j - 1] == 1:
                    check[i*j - 1] = 0
                    break
                
print(check.count(1))

'''


N = int(input())

i = 1
ans = 0
while i*i <= N:
    i += 1
    ans += 1
    
print(ans)



''' 또 다른 답
N = int(input())

ans = int(N**0.5)
print(ans)
'''