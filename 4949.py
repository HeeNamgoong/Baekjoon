import sys
input = sys.stdin.readline

while True:
    brackets = list(input())
    if brackets[0] == ".":
        break

    stack = []
    ans = True
    
    for bracket in brackets:
        if '(' == bracket or '[' == bracket:
            stack.append(bracket)
        elif ')' == bracket:
            if len(stack) == 0 or stack[-1] != '(':
                ans = False
                break
            stack.pop()
        elif ']' == bracket:
            if len(stack) == 0 or stack[-1] != '[':
                ans = False
                break
            stack.pop()
            
    if (len(stack) == 0) and ans == True:
        print("yes")
    else:
        print("no")