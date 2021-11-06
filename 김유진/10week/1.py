def solution(sizes):
    maxList=[]
    minList=[]

    for i in sizes:
        maxList.append(max(i[0],i[1]))
        minList.append(min(i[0],i[1]))
    
    maxList.sort()
    minList.sort()

    return maxList[-1]*minList[-1]
