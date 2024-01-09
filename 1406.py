''' 시간 초과!! 연결 리스트로 다시 풀기
import sys

input = sys.stdin.readline

str_ = list(input())
del str_[-1]

cursor = "|"
str_.append(cursor)
idx = len(str_) - 1 # 커서의 현재 위치

M = int(input())

for i in range(M):
    com = list(map(str, input().split()))
    
    if com[0] == "L":
        if idx == 0:
            pass
        else:
            str_.insert(idx - 1, cursor)
            del str_[idx + 1]
            idx -= 1

    elif com[0] == "D":
        if idx == len(str_) - 1:
            pass
        else:
            str_.insert(idx + 2, cursor)
            del str_[idx]
            idx += 1
        
    elif com[0] == "B":
        if idx == 0:
            pass
        else:
            del str_[idx - 1]
            idx -= 1
            
    elif com[0] == "P":
        str_.insert(idx, com[1])
        idx += 1

for i in str_:
    if i == "|":
        pass
    else:
        print(i)

'''



import sys

input = sys.stdin.readline

str_ = input().rstrip() + "|"
size = len(str_) -1
idx = size # 커서의 현재 위치

for i in range(int(input())):
    com = list(map(str, input().split()))
    
    if com[0] == "L":
        if idx > 0:
            idx -= 1

    elif com[0] == "D":
        if idx < size:
            idx += 1
        
    elif com[0] == "B":
        if idx > 0:
            str_ = str_[:idx-1] + str_[idx:]
            idx -= 1
            
    elif com[0] == "P":
        str_ = str_[:idx] + com[1] + str_[idx:]
        idx += 1
    
print(str_.replace("|", ""))
