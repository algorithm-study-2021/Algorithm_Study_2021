def solution(n):
    answer = 0
    
    new_li=list(str(n))
    new_li = list(map(int, new_li))
    new_li.sort(reverse=True)
    new_li=list(map(str,new_li))
    new_li=''.join(new_li)
    
    answer=int(new_li)
    return answer
