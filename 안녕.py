# N = int(input())

# L = list(map(int, input().split()))
# J = list(map(int, input().split()))
# dict_ = []

# for i in range(N):
#     dict_.append((L[i], J[i]))

# dict_.sort(key=lambda x: x[1], reverse=True)

# health = 100
# ans = 0

# for i in dict_:
#     health -= i[0]

#     if health <= 0:
#         if ans == 0 and N == 1:
#             break
#         else:
#             health += i[0]
#             continue
#     else:
#         ans += i[1]

# print(ans)










N = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))
dict_ = []

for i in range(N):
    dict_.append((L[i], J[i]))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

health = 100
ans = 0