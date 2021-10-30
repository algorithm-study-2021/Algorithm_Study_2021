def solution(n):
    ans = 0
    
    while n!=0:
        if n%2==0: #짝수라면
            n=n//2
        elif n%2!=0: #홀수라면
            n=n-1
            ans=ans+1

    return ans
#1. n에서부터 거꾸로 0까지 내려가기
#홀수면 -1, 짝수면 2로 나누면서 0까지 내려감
