def solution(clothes):
    #딕셔너리 생성
    info=dict()

    for i in clothes:
        if info.get(i[1])==None:
            info[i[1]]=1
        else:
            info[i[1]]+=1

    
    #value값만 리스트로 생성
    valInfo=list(info.values())
    
    sum=1
    for i in valInfo:
        sum*=i+1 #안 입는 경우까지 경우로 포함
    
    return sum-1 #모두 안 입는 경우 제외

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))