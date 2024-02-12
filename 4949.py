import sys
input = sys.stdin.readline


    
while True:
    brackets = input()
    
    if brackets == ".":
        break


    # if brackets[0] == ')' or brackets[0] == ']':
    #     return "no"
    
    
    stack = []
    stack_ = []
    for bracket in brackets:
        if '(' == bracket:
            stack.append(bracket)
        elif ')' == bracket:
            if len(stack) == 0:
                print("no")
            stack.pop()
            
        elif '[' == bracket:
            stack_.append(bracket)
        elif ']' == bracket:
            if len(stack_) == 0:
                print("no")
            stack_.pop()

            
    if (len(stack) == 0) and (len(stack_) == 0):
        print("yes")
    else:
        print("no")
    


        
            
