'''
import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
num_copied = num[:]
ans = []

idx = 0
for i in range(N):
    
    if num[idx] > 0:
        idx += num[idx]
    else:
        idx -= num[idx]
    ans.append(idx + 1)
    del num_copied[idx]
    
    num[idx]


print(ans)


idx = 0
del num_copied[0]

for i in range(N-1):
    if num[idx] > 0:
        idx += num[idx]
        ans.append(idx + 1)
        del num_copied[idx - 1]
        idx = idx - i
    else:
        idx -= num[idx]
        ans.append(idx + 1 + N)
        del num_copied[idx]
        idx = idx
    


'''


import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
num_copied = num[:]
ans = []

idx = 0
idx_copied = 0
ans.append(idx + 1)
del num[0]

# for i in range(N-1):
#     if num[idx] > 0:
#         idx += num[idx]
#         ans.append(idx + 1)
#         del num[idx - 1]
#         ###
#         idx = idx - 1
#     else:
#         idx -= num[idx]
#         ans.append(idx + 1 + N)
#         del num[idx]
#         idx = idx


for i in range(N-1):
    if num_copied[idx_copied] > 0:
        idx = num_copied[idx]
        idx_copied = num_copied[idx]
        ans.append(idx + 1)
        del num[idx - 1]
        ###
        #idx = idx - 1
    else:
        idx = num_copied[idx]
        ans.append(idx + 1 + N)
        del num[idx]
        idx = idx

    


