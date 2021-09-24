def solution(s):
    stack=[]

    for i in s:
        if i=='(':
            stack.append(i)
        else: #')'
            try:
                if(stack.pop()!='('): return False
            except:
                return False

    return len(stack)==0

print(solution("(()("))