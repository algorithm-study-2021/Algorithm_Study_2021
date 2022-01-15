def solution(d, budget):
    #d 정렬
    d.sort()
    count=0

    for i in d:
        if budget<i:
            break
        else:
            count+=1; budget-=i

    return count
