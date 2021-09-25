def solution(s):
    s=list(s)
    
    num=0
    for i in range(0,len(s)):
        if s[i]==')':
            num-=1
        elif s[i]=='(':
            num+=1
        if num<0:
            return False

    if num==0:
        return True
    elif num>0:
        return False
