def solution(s):
    s=s.lower()
    s=list(s)
    s[0]=s[0].upper()
    s=''.join(s)
    for i in range(0,len(s)):
        if s[i]==" " and i!=len(s)-1:
            s=list(s)
            s[i+1]=s[i+1].upper()
            s=''.join(s)
    answer=s
    return answer
