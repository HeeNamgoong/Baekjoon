# KMP



# def compute_pi(p):
#     m = len(p)
#     pi = [0] * (m+1)  # pi 배열 초기화
#     j = 0         # 접두사-접미사 일치 길이

#     for i in range(1, m):  # i는 1부터 시작 (0은 항상 0)
#         while j > 0 and p[i] != p[j]:
#             j = pi[j - 1]  # 일치하지 않으면 이전 일치 상태로 이동

#         if p[i] == p[j]:   # 일치하면
#             j += 1
#             pi[i] = j

#     return pi

import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

def compute_pi(p):
    m = len(p)
    pi = [0] * m
    i = 1
    j = 0

    while i < m:
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            i += 1
        elif j == 0:
            pi[i] = j
            i += 1
        else:
            j = pi[j-1]
    return pi

pi = compute_pi(P)

n, m = len(T), len(P)
i, j = 0, 0
ans = 0
idx = []
while i < n:
    if T[i] == P[j]:
        i += 1
        j += 1        
    elif j == 0:
        i += 1
    else:
        j = pi[j-1] # 다시 앞으로 되돌아 가라


    if j == m: # j가 끝까지 왔으면 매칭 완료
        ans += 1
        idx.append(i-j+1) # 매칭이 시작되는 T의 인덱스
        j = pi[j-1] # j 초기화
        

print(ans) # T 중간에 P가 몇 번 나타나는지
print(*idx)


# def compute_pi(p):
#     m = len(p)
#     pi = [0] * m
#     i = 1
#     j = 0

#     while i < m:
#         if p[i] == p[j]:
#             j += 1
#             pi[i] = j
#             i += 1
#         else:
#             if j == 0:
#                 pi[i] = j
#                 i += 1
#             else:
#                 j = pi[j-1]
#     return pi

# pi = compute_pi(P)
# print(pi)
# n, m = len(T), len(P)
# i, j = 0, 0
# ans = 0
# idx = []
# while i < n:
#     if T[i] == P[j]:
#         i += 1
#         j += 1
#     else:     
#         if j == 0:
#             i += 1
#         else:
#             j = pi[j-1] # 다시 앞으로 되돌아 가라


#     if j == m: # j가 끝까지 왔으면 매칭 완료
#         ans += 1
#         idx.append(i-j+1)
#         j = 0 # j 초기화
        

# print(ans) # T 중간에 P가 몇 번 나타나는지
# print(*idx)