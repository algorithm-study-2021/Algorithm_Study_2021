def provePrime(input):
    for i in range(2,(input//2)+1):
        if input%i==0:
            return False 
    return True

def solution(n):
    res=0
    for i in range(2,n+1):
        if provePrime(i): res+=1
    return res

print(solution(10))
print(solution(5))