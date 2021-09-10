def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m)) #최대공약수
    answer.append((n*m)//answer[0]) #최소공배수
    
    return answer

def gcd(a,b):
    if b>a:
        a,b=b,a
    if b==0:
        return a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
