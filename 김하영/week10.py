### 1 2개 이하로 다른 비트
## x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
## 입출력 예  [2,7]->[3,11]
def solution(numbers):
    answer = []
    for number in numbers:
        x = tobinary(number)
        if len(x) == 0: #0인 경우
            answer.append(1)
        elif len(x) == 1: #1인 경우
            answer.append(2)
        else: #그 외 숫자
            if x[-1] =='0':
                x = x[:-1] + '1'
            elif x[-2]+x[-1] == '01':
                x = x[:-2] + '10'
            else:
                x = '0' + x
                index = x.rfind('0')
                x = x[:index] + '10' + x[index+2:]
            answer.append(frombinary(x))
    return answer

def tobinary(n): #이진수로
    answer = ''
    while n!=0:
        answer = str(n%2) + answer
        n = n//2
    return answer

def frombinary(n): #십진수로
    answer = 0
    for i in range(len(n)):
        answer += int(n[-(i+1)])*(2**i)
    return answer

### 2 [1차] 프렌즈4블록
## 4개가 붙어있을 경우 사라지면서 / 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져
## 입출력 예  4,5 -> ["CCBDE", "AAADE", "AAABF", "CCBBF"]
def solution(m, n, board):
    answer = 0
    b=[]
    for i in range(len(board)): #글자별로 나누기
        b.append(list(board[i]))
    while True:
        starts=[]
        for i in range(m-1): #4개의 시작점 찾기
            for j in range(n-1):
                if b[i][j]!=0 and b[i][j] == b[i][j+1] and b[i][j]==b[i+1][j] and b[i][j]==b[i+1][j+1]:
                    starts.append([i,j])
        if len(starts)==0:
            break
        else: #지워지는 블록
            for i in range(len(starts)):
                if b[starts[i][0]][starts[i][1]]!=0:
                    b[starts[i][0]][starts[i][1]]=0
                    answer += 1
                if b[starts[i][0]][starts[i][1]+1]!=0:
                    b[starts[i][0]][starts[i][1]+1]=0
                    answer += 1
                if b[starts[i][0]+1][starts[i][1]]!=0:
                    b[starts[i][0]+1][starts[i][1]]=0
                    answer += 1
                if b[starts[i][0]+1][starts[i][1]+1]!=0:
                    b[starts[i][0]+1][starts[i][1]+1]=0
                    answer += 1
            for i in range(n): #내려오기
                for j in range(m-1, 0, -1):
                    if b[j][i]==0:
                        for k in range(j-1, -1, -1):
                            if b[k][i]!=0:
                                b[j][i]=b[k][i]
                                b[k][i]=0
                                break
    return answer

#실패
### 3 피로도
## 유저가 탐험할수 있는 최대 던전 수를 return
## 입출력 예  80, [[80,20],[50,40],[30,10]] -> 3
def solution(k, dungeons):
    answer = 0
    for i in range(len(dungeons)):
        dungeons[i].insert(0,dungeons[i][0]-dungeons[i][1]) #두 값의 차이
    dungeons.sort(key=lambda x: (-x[0]))
    for i in range(len(dungeons)):
        if dungeons[i][1] <= k:
            answer += 1
            k -= dungeons[i][2]
    return answer