def solution(n):
    answer = 0

    new_li=list(str(n))
    new_li=list(map(int,new_li))
    
    for i in range(0,len(new_li)):
        answer+=new_li[i]
    
    return answer
