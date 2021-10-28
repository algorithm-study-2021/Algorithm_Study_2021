def solution(n):
    ans=0
    while(1):
        if n==1: ans+=1; return ans
        
        if n%2==0:  n=n//2
        else: ans+=1; n=n//2

print(solution(5000))