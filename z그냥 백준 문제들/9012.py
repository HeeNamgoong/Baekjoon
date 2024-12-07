
'''
import sys
input = sys.stdin.readline

for i in range(int(input())):
    brackets = list(str(input()))
    brackets.pop()
    
    cnt = 0
    for i in range(len(brackets)):
        if "(" == brackets[i]:
            cnt += 1
        else:
            cnt -= 1     
    
    if cnt == 0:
        print("YES")
    else:
        print("NO")
'''


import sys
input = sys.stdin.readline

def VPS():
    
    brackets = list(str(input()))
    brackets.pop()
    
    if brackets[0] == ')':
        return "NO"
    
    stack = []
    for bracket in brackets:
        if '(' == bracket:
            stack.append(bracket)
        elif len(stack) == 0:
            return "NO"
        else:
            stack.pop()
    
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
    
for i in range(int(input())):
    print(VPS())
            
                
