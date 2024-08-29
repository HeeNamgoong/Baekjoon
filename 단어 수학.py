# 가중치 부여 안 한 코드 ㅜㅜ
'''
import sys
input = sys.stdin.readline
N = int(input())

alphas = []
for _ in range(N):
    alpha = input().rstrip()
    alphas.append(alpha)

alphas = sorted(alphas, key = lambda x: len(x))


ls = [[] for _ in range(10)]
for alpha in alphas:
    for i in range(len(alpha), 0, -1):
        ls[len(alpha) - i].append(alpha[i-1])

ls = ls[:len(alpha)]
print(ls[::-1])
num = [i for i in range(9, -1, -1)]

alphabet = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False, 'J': False}
dict_ = {}
cnt = 0
for i in range(len(ls[::-1])):
    for j in range(len(ls[::-1][i])):
        if alphabet[ls[::-1][i][j]] == False:
            dict_[ls[::-1][i][j]] = num[cnt]
            alphabet[ls[::-1][i][j]] = True
            cnt += 1
        

print(dict_)


sum_ = 0
for j in range(len(alphas)):
    for k in range(len(alphas[j])):
        sum_ += dict_[alphas[j][k]] * 10**(len(alphas[j]) - k - 1)
print(sum_)
'''

# Runtime Error(KeyError) - 딕셔너리에 해당하는 key가 없을 때 발생
# 알파벳이 10개라 해서 A ~ B만 존재하는 것이 아님!
'''
import sys
input = sys.stdin.readline
N = int(input())

alphas = []
for _ in range(N):
    alpha = input().rstrip()
    alphas.append(alpha)

dict_ = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
for i in range(len(alphas)):
    for j in range(len(alphas[i])):
        dict_[alphas[i][j]] += 10 ** (len(alphas[i]) - j - 1) # 가중치 부여
dict_ = sorted(dict_.items(), key = lambda x: x[1], reverse=True)

num_dict = {}
num = 9
for key, value in dict_:
    if value == 0:
        break
    else:
        num_dict[key] = num
        num -= 1

sum_ = 0
for j in range(len(alphas)):
    for k in range(len(alphas[j])):
        sum_ += num_dict[alphas[j][k]] * 10**(len(alphas[j]) - k - 1)
print(sum_)
'''

# 딕셔너리 KeyError 해결
import sys
input = sys.stdin.readline
N = int(input())

dict_ = {}
alphas = []
for _ in range(N):
    alpha = input().rstrip()
    alphas.append(alpha)
    for i in range(len(alpha)):
        if alpha[i] in dict_:
            dict_[alpha[i]] += 10 ** (len(alpha) - i - 1)  # 가중치 부여
        else:
            dict_[alpha[i]] = 10 ** (len(alpha) - i - 1)
    
dict_ = sorted(dict_.items(), key = lambda x: x[1], reverse=True)

num_dict = {}
num = 9
for key, value in dict_:
    num_dict[key] = num
    num -= 1

sum_ = 0
for j in range(len(alphas)):
    for k in range(len(alphas[j])):
        sum_ += num_dict[alphas[j][k]] * 10**(len(alphas[j]) - k - 1)
print(sum_)