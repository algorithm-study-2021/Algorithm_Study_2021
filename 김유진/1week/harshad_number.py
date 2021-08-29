def solution(x): #양의정수 
    answer = True
    #문자열로 바꿔서 하나씩 추출
    str_x=str(x)
    add_total=0

    for i in str_x:
        add_total+=int(i)
    
    if x%add_total!=0:
        answer=False
    return answer

print(solution(11))