def test(people,limit): #두명 
    sum=0
    boat=0
    take=0
    for i in people:
        if sum+i<limit and take<2:
            sum+=i
            take+=1
        elif sum+i==limit and take<2:
            sum=0
            take=0
            boat+=1
        else:
            sum=i
            take=1
            boat+=1
    if take>0: boat+=1
    
    return boat

#보트에 탈 수 있는 사람은 단 두명 
def solution(people, limit):
    people.sort()
    
    #중간값을 기준으로 나눔
    mid=len(people)//2
    low=people[:mid]
    high=people[mid:]
    high.sort(reverse=True)

    boat=0
    for i in range(mid):
        ok=False
        for k in range (len(high)):
            if low[0]+high[k]<=limit:
                ok=True; num=k
                break
        if ok==True:
            boat+=1
            low=low[1:]
            del high[num] #효율성 문제 구간 
        else:
            break

    #남은 리스트에서 
    boat+=test(low,limit)
    boat+=test(high,limit)

    return boat

print(solution([50, 50, 50, 50,50],100))

"""
두 개로 나누지 않고
앞이랑 뒤랑 비교해서 해야할 듯함 
"""