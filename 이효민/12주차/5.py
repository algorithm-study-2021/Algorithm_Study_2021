#위장
def solution(clothes):
    answer = 1
    
    count=[]
    clas=[]
    for i in range(0,len(clothes)):
        count.append(clothes[i][1])
        if clothes[i][1] not in clas:
            clas.append(clothes[i][1])
        
    for j in range(0,len(clas)):
        answer*=(count.count(clas[j])+1)
        
    answer-=1
    
    return answer
