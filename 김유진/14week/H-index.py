def findHval(idx,cit):
    #idx 부터 리스트 끝까지 cit[1] 총합 
    sum=0
    for i in range (idx,len(cit)):
        sum+=cit[i][1]
    return sum

def solution(citations):
    #(인용횟수,논문 수) 로 자료구조 변경
    cit=dict()
    for i in citations:
        if(cit.get(i)==None):
            cit[i]=1
        else:
            cit[i]+=1 

    cit=list(zip(cit.keys(),cit.values()))

    #cit 정렬
    cit.sort(key=lambda x:x[0])

    print(cit)
    
    #처음부터 h-index 적용되지 않을 때까지 반복문
    for i in range(0,len(cit)):
        if cit[i][0]>findHval(i,cit):
            return cit[i-1][0]


print(solution([3, 0, 6, 1, 5]))

#뭔말인지이해가안감 ㅗ 