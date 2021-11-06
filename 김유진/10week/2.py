def allSearch(target,tower,without): #송전탑 번호
    if without in tower[target][1]:
        tower[target][1].remove(without)

    if len(tower[target][1])==1: return 1
    else:
        for i in tower[target][1]:
            if i !=without:
                return 1+allSearch(i,tower,target)

def solution(n, wires):
    tower=[None for i in range (n)]

    #송전탑 연결 정보 tower List에 넣기 
    for i in wires:
        first=i[0]-1;second=i[1]-1 
        if tower[first]==None:
            tower[first]=[first,[second]]
        else:
            tower[first][1].append(second)
        
        if tower[second]==None:
            tower[second]=[second,[first]]
        else:
            tower[second][1].append(first)

    #제일 연결이 많은 거 찾기
    tower.sort(key=lambda x:-len(x[1]))
    max=tower[0] #가장 연결 많은 송전탑
    maxConnected=tower[0][1] #연결된 송전탑 list 

    #연결된 송전탑 중 연결 많은 송전탑 찾기(이거 말고 총 연결된 갯수가 많은 걸 찾아야 함 ㅠ )
    for i in tower:
        if i[0] in maxConnected:
            second=i
            break

    print(max, second)
    #연결 송전탑 개수 차이
    maxNum=0
    for i in max[1]:
        maxNum+=allSearch(i,tower,second[0])

    secondNum=0
    for i in second[1]:
        secondNum+=allSearch(i,tower,max[0])

    return abs(maxNum-secondNum)

print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

"""
연결된 송전탑 중 최대 연결수 이 부분에서 다시 짜야함 (지금은 밑에 거까지 고려 안 함) - 트리구조임!!! 
"""