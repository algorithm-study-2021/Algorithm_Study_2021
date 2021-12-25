#Dijkstra 최단경로 알고리즘
def searchU(dist,found):
    min=500001
    minpos=-1
    for i in range(1,len(dist)):
        if dist[i]<min and found[i]==False:
            min=dist[i]
            minpos=i
    return minpos

def solution(N, road, K):
    #dist, weitght 리스트 생성, 초기화
    weight=[[500001 for j in range(N+1)]for i in range(N+1)]
    #weight 자기 자신 0
    for i in range (len(weight)):
        weight[i][i]=0

    for i in road:
        if weight[i[0]][i[1]]>i[2]:
            weight[i[0]][i[1]]=i[2]; weight[i[1]][i[0]]=i[2]

    dist=weight[1][:]

    found=[False]*(N+1)

    for i in range(N): #알고리즘 실행 반복
        u=searchU(dist,found)
        found[u]=True

        for w in range(1,N+1):
            if not found[w]:
                if dist[u]+weight[u][w]<dist[w]:
                    dist[w]=dist[u]+weight[u][w]
    
    #dist 처리
    #k시간 이하에 배달 가능한 마을의 개수
    sum=0
    for t in range(1,len(dist)):
        if dist[t]<=K:
            sum+=1

    return sum