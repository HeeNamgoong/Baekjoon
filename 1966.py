import sys

input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int, input().split())
    
    importance = list(map(int, input().split()))
    
    doc = []
    for i in range(N):
        doc.append((importance[i], i)) # 중요도와 문서의 번호 매칭 (중요도가 앞인 이유 : max값 쉽게 찾기 위해서)
    
    print(doc)
   

    cnt = 0
    while True:
        if doc[0][0] == max(doc)[0]:
            cnt += 1
            
            if doc[0][1] == M:
                print(cnt)
                break
            else:
                del doc[0]
            
        else:
            doc.append(doc[0])
            del doc[0]
        print(doc)
            

