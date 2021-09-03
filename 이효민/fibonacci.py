def solution(n):
    num=fibo(n) #피보나치 수열에서 n번째 값
    num%=1234567
    answer = num
    return answer

def fibo(n):
    result=[]
    result.append(0)
    result.append(1)
    for i in range(2,n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]
