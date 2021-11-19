def solution(people, limit):
    people.sort()
    print(people)
    idx=0; idx2=len(people)-1
    out=0

    while 1:
        if idx==idx2: return out
        
        print(idx,", ",idx2)
        if people[idx]+people[idx2]>limit: idx2-=1
        else: 
            if abs(idx-idx2)==1: return out+1
            else: idx+=1; idx2-=1 

        out+=1 #보트 개수

print(solution([70, 50, 80, 50],100))