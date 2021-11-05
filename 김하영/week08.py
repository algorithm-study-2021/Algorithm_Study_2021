### 1 최소직사각형
## 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return
## 입출력 예  [[60, 50], [30, 70], [60, 30], [80, 40]]->4000 / [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]->133
def solution(sizes):
    for size in range(len(sizes)): # 큰 수를 가로 길이로
        if sizes[size][0] < sizes[size][1]:
            sizes[size][0], sizes[size][1] = sizes[size][1],sizes[size][0]
    max1 = max(sizes)[0] #가로 길이 중 최댓값
    max2 = sorted(sizes, key=lambda x:x[1], reverse=True)[0][1]
    answer = max1*max2
    return answer

### 2 전력망을 둘로 나누기
## 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할
## 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게
## 입출력 예  [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]->3
def solution(n, wires):
    answer=0
    difference = [] # 모든 전선의 끊김에 대한 탑 갯수 차이
    for i in range(len(wires)):
        tempw = wires[:]
        top1 = wires[i][0]
        top2 = wires[i][1]
        del tempw[i] #하나의 연결 제거
        difference.append(lnum(top1, top2, tempw)) 
    answer = min(difference)
    return answer

def lnum(top1,top2,tempw):#송전탑 갯수 차이 반환 함수
    wires1 = [top1]
    wires2 = [top2]
    while len(tempw)!=0:
        for i in range(len(tempw)-1, -1, -1): #두 전력망으로 분류
            if tempw[i][0] in wires1:
                wires1.append(tempw[i][1])
                del tempw[i]
            elif tempw[i][1] in wires1:
                wires1.append(tempw[i][0])
                del tempw[i]
            elif tempw[i][0] in wires2:
                wires2.append(tempw[i][1])
                del tempw[i]
            elif tempw[i][1] in wires2:
                wires2.append(tempw[i][0])
                del tempw[i]
    answer = max(len(wires1)-len(wires2), len(wires2)-len(wires1)) #탑 차이의 절대값
    return answer

### 3 교점에 별 만들기
## Ax + By + C = 0/ n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별
def solution(line):
    answer = []
    location = []
    for l1 in range(len(line)-1):
        for l2 in range(l1+1, len(line)):
            if line[l1][0]*line[l2][1] - line[l1][1]*line[l2][0] == 0: # 평행 또는 일치
                break
            a = line[l1][0]
            b = line[l1][1]
            e = line[l1][2]
            c = line[l2][0]
            d = line[l2][1]
            f = line[l2][2]
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            if isint(x) and isint(y): #정수 좌표 추가
                location.append([int(x),int(y)])
    minx = sorted(location)[0][0]
    maxx = sorted(location, reverse=True)[0][0]
    miny = sorted(location, key = lambda x:x[1])[0][1]
    maxy = sorted(location, reverse=True, key = lambda x:x[1])[0][1]
    size = [['.'for j in range(maxx-minx+1)]for i in range(maxy-miny+1)] #사이즈 초기화
    
    for loca in location: #.을 *로
        size[loca[1]-miny][loca[0]-minx] = '*'
    
    for i in range(len(size)): 
        row = ''.join(size[i]) # 문자열로 
        answer = [row]+answer # 리스트의 앞에 추가
    return answer

def isint(num): #정수 판별 함수
    dotloca = str(num).find('.')
    for i in range(dotloca+1, len(str(num))):
        if str(num)[i] != '0':
            return False
    return True

#실패
### 4 구명보트
## 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
## 구명보트 개수의 최솟값을 return
## 입출력 예  [70, 50, 80, 50],100->3 / [70, 80, 50],100->3
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while len(people)!=0:
        if len(people)!=1:
            if people[0] + people[-1] <= limit:
                del people[-1]
        del people[0]
        answer += 1
    return answer

### 5 주식가격
## 가격이 떨어지지 않은 기간은 몇 초인지를 return
## 입출력 예  [1, 2, 3, 2, 3]->[4, 3, 1, 1, 0]
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time+=1
            if prices[j] < prices[i]:
                break
        answer.append(time)
    return answer