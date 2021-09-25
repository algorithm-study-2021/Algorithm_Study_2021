def solution(s):
    num=0
    for i in range(0,len(s)):
        if s[i]=='p' or s[i]=='P':
            num+=1
        elif s[i]=='y' or s[i]=='Y':
            num-=1
    
    if num==0:
        answer=True
    else:
        answer=False

    return answer
