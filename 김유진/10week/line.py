from collections import deque

#BFS 이용
def search(cut,tower_info): #잘린 간선 [a,b], wires 배열, t_info
    #a에 대해 BFS (a-b는 지나지 않도록)
    visited=[] ; queue=deque()
    a=cut[0]; b=cut[1]
    res=0

    visited.append(a)#현재 시작점은 visited에 추가 

    #queue에 b 제외 append(tower_info[a]를 - a에 연결된 송전탑)
    for i in tower_info[a]:
        if i!=b:
            queue.append(i)

    while len(queue)!=0:
        node=queue.popleft()
        visited.append(node) #pop할 때, visited한 것 

        for i in tower_info[node]:
            if i not in visited:
                queue.append(i)

        res+=1

    return res

def solution(n, wires):
    #wires에 대한 graph 생성 [idx,[연결된 송전탑 idx]]
    tower_info=[[]for i in range(n+1)] #0부터 생성되어서 1부터 고려(0 index 무시)
    for i in wires:
        tower_info[i[0]].append(i[1])
        tower_info[i[1]].append(i[0])

    min=9999
    for i in range(len(wires)):
        #i 간선을 끊기
        a=wires[i][0]; b=wires[i][1] 
        aVal=search([a,b],tower_info); bVal=search([b,a],tower_info)
        abVal=abs(aVal-bVal)

        if min>abVal: min=abVal
    
    return min