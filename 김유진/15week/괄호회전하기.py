def check(s):
    stack=[]
    for c in s:
        if c in ('{','(','['):
            stack.append(c)
        elif c in ('}',')',']'):
            if len(stack)==0: return False
            else:
                val=stack.pop(-1)
                if  (c=='}' and val!='{') or \
                    (c==')' and val!='(') or \
                    (c==']' and val!='['):
                    return False

    return len(stack)==0

def rotate(s):
    #왼쪽으로 한 칸 회전
    left=s[0]
    s=s[1:]
    s+=left

    return s

def solution(s):
    s=list(s) #mutable 하도록 
    sum=0

    if check(s):
        sum+=1

    for i in range(1,len(s)):
        s=rotate(s)

        if check(s):
            sum+=1

    return sum

print(solution("}]()[{"))