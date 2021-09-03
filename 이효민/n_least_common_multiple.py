def solution(arr):
    answer=1
    num=len(arr)
    prime=[]
    for i in range(0,len(arr)):
        in_prime=primeReturn(arr[i])
        if len(in_prime)!=0:
            prime.append(in_prime)
    
    for j in range(1,len(prime)):
        least_common=1
        for i in range(0,len(prime[0])):
            if prime[0][i] in prime[j]:
                prime[j].remove(prime[0][i])
        for e in range(0,len(prime[0])):
            least_common*=prime[0][e]
        for k in range(0,len(prime[j])):
            least_common*=prime[j][k] 
        prime[0]=primeReturn(least_common)
    
    for v in range(0,len(prime[0])):
        answer*=prime[0][v]
            
    return answer

def primeReturn(num):
    in_prime=[]
    n=2
    while n<=num:
        if num%n==0:
            num/=n
            in_prime.append(n)
        else:
            n+=1
    return in_prime
