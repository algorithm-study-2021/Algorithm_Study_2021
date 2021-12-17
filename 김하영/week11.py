##실패-시간초과
### 1 큰 수 만들기
## k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
## 입출력 예  "1924",2->"94" / "1231234",3->"3234" / "4177252841",4->"775841"
def solution(number, k):
    answer = ''
    start=-1 #범위 내 최댓값의 인덱스
    for i in range(k+1,len(number)+1):
        #범위 내에서 최댓값 찾기
        maxc = max(number[start+1:i])
        answer += str(maxc)
        start=number.index(maxc, start+1, i)
    return answer

### 2 카펫
## 갈색 격자의 수, 노란색 격자의 수가 매개변수로 주어질 때 카펫의 가로, 세로 크기
## 입출력 예  10,2->[4, 3] / 8,1->[3, 3] / 24,24->[8, 6]
def solution(brown, yellow):
    answer = []
    sumb = (brown+4)//2 #가로+세로
    #yello=가로*세로-brown
    #가로*세로=yellow+brown
    for row in range(3,sumb-2):
        col = sumb-row
        if row*col == brown+yellow:
            answer.append(col)
            answer.append(row)
            break
    return answer

### 3 H-Index
## 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
## 입출력 예  [3, 0, 6, 1, 5]->3
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)): #리스트 내 숫자 있는 경우
        if i+1 >= citations[i]: #h번 이상 인용 논문 수
            if i==len(citations)-1:# 마지막 차례
                answer = citations[i]
                break
            elif citations[i+1] < citations[i]:#다음수가 같지 않는
                answer = citations[i]
                break
    temp=len(citations) #리스트 내 숫자 없는 경우를 위한 변수
    for i in range(len(citations)-1,-1,-1):
        if citations[i] <= temp:
            temp -=1
    answer = max(answer, temp)
    return answer
#테스트케이스
# print(solution([3,0,6,1,5]))#3
# print(solution([20,19,18,1]))#3
# print(solution([22,42]))#2
# print(solution([5,5,5,5]))#4

### 4 다리를 지나는 트럭
## 다리를 건너려면 최소 몇 초가 걸리는지
## 입출력 예  2,10,[7,4,5,6]->8 / 100,100,[10,10,10,10,10,10,10,10,10,10]->110
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge=[]#다리 건너는 트럭
    ontime=[] #트럭마다 남은 시간
    over=[]#지난 트럭
    numt=len(truck_weights) #트럭 수
    while len(over)!=numt:#1초마다 판단
        if len(ontime)!=0 and ontime[0]==0:
            over.append(onbridge.pop(0))
            ontime.pop(0)
        #대기 남아 있고 무게 괜찮다면 입장
        if len(truck_weights) != 0 and sum(onbridge)+truck_weights[0] <= weight:
            onbridge.append(truck_weights.pop(0)) #건너는 트럭 추가
            ontime.append(bridge_length)
        #print(ontime)
        answer +=1
        for i in range(len(ontime)):
            ontime[i] -= 1
    return answer

### 5 위장
## 서로 다른 옷의 조합의 수를 return
## 입출력 예  [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]->5
def solution(clothes):
    answer = 1
    #종류별로 나누기
    cate=[]
    divide = []
    for i in range(len(clothes)):
        if clothes[i][1] not in cate: #없는 종류 추가
            cate.append(clothes[i][1])
            divide.append(1)
        else: #이미 있는 종류
            for j in range(len(divide)):
                if clothes[i][1] == cate[j]:
                    divide[j] = divide[j]+1
                    break
    
    for i in range(len(cate)):
        answer *= (divide[i]+1) #경우 곱하기
    answer -= 1 #아무 옷 없는 경우 빼기
    return answer

### 6 배달
## 음식 주문을 받을 수 있는 마을의 개수를 return
## 입출력 예  6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4->4
