def solution(n):
    answer = 0
    if int(n**(1/2))==n**(1/2): #n이 제곱수인 경우
        answer=(n**(1/2)+1)**2
    else:
        answer=-1
        
    return answer
