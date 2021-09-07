def gcd(a,b):
    #크기비교
    if a>b: a,b=b,a

    while b!=0:
        r=a%b
        a=b
        b=r
    
    return a

def solution(n, m):
    gcd_value=gcd(n,m)

    #lcm
    lcm_value=n*m//gcd_value

    answer=[gcd_value,lcm_value]
    return answer
