def outQueue(queue):
    sumWeight=0
    size=len(queue)
    #문제점) [pop 때문에 한칸 땡겨짐] -> index로 접근 시 일치하지 않음
    for i in range(size):
        if queue[0][1]==0:
            sumWeight+=queue[0][0]
            queue.pop(0)
        else: 
            break
    return sumWeight

def reduceQueue(queue):
    for i in range(len(queue)):
        queue[i][1]-=1

def solution(bridge_length, weight, truck_weights):
    #총 걸리는 시간: bridge_length

    time=1; queue=[]; sumWeight=0
    while 1:
        #반복문 초반에 처리 
        #queue에 있는 트럭 0초면 pop
        sumWeight-=outQueue(queue)

        #종료 조건 
        if len(truck_weights)==0 and len(queue)==0: 
            break
        
        if len(truck_weights)!=0:
            if truck_weights[0]+sumWeight<=weight:
                #무게 진입 가능
                w=truck_weights.pop(0)
                sumWeight+=w
                queue.append([w,bridge_length]) #[무게, 남은 길이]
                #queue에 해당 트럭 넣기

        #일괄 처리
        #queue에 있는 트럭 1초씩 감소
        reduceQueue(queue)
        #시간 증가
        time+=1

    return time