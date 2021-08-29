def solution(n):
    #피보나치수 계산
    fibo1=0
    fibo2=1

    answer=0

    for i in range(2,n+1):
        answer=fibo1+fibo2
        fibo1=fibo2
        fibo2=answer

    return answer%1234567

print(solution(5))
