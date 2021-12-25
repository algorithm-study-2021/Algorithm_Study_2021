#h-index
def solution(citations):
    answer = 0
    
    if 0 not in citations:
        citations.append(0)
    
    citations.sort(reverse=True)
    
    num=0
    max=0
    min=0
    for i in range(0,len(citations)):
        if citations[i]==i+1:
            answer=i+1
            return answer
        elif citations[i]<i+1:
            num=i
            min=citations[i]
            max=citations[i-1]
            break
    
    print(min,max,num)
    for j in range(min,max+1):
        if j==num:
            answer=num
    
    return answer
