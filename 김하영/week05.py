### 1 [3차]압축
## LZW(Lempel–Ziv–Welch) 압축을 구현
def solution(msg):
    answer = []
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    start = 0
    end = 1
    while end <= len(msg):
        start = end-1
        end = start + 1
        check = True
        while check:# end를 정하기 위한 반복문
            end += 1
            if msg[start:end] not in dic or end > len(msg):
                check = False
        if end <= len(msg): # 마지막 추가를 제외하기 위한 조건
            dic.append(msg[start:end])
        answer.append(dic.index(msg[start:end-1])+1)
    return answer

### 2 가장 큰 정사각형 찾기
## 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return
## 입출력 예  [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]->9
#효율성 실패
def solution(board):
    answer=0
    for row in range(len(board)):
        for col in range(len(board[0])):
            side = 0
            if board[row][col] != 0:
                check = True
                while check:
                    side += 1
                    if (row+side >= len(board)) or (col+side >= len(board[0])): #board 범위 넘으면
                        break
                    for cside in range(row, row+side+1): # 세로줄 확인
                        if board[cside][col+side] == 0:
                            check = False
                            break
                    if check == True:
                        for rside in range(col, col+side): # 가로줄 확인
                            if board[row+side][rside] == 0:
                                check = False
                                break
            answer = max(answer, side)
    return answer*answer

### 3 [3차] 방금그곡
#실패

### 4 방문 길이
## 캐릭터가 처음 걸어본 길의 길이
## 입출력 예  "ULURRDLLU"->7 / "LULLLLLLU"->7
def solution(dirs):
    answer = 0
    row, col = 0,0
    nrow, ncol = 0,0
    paths=[]
    for i in dirs:
        if i=='L': #움직일 좌표
            nrow = row
            ncol = col-1
        elif i=='R':
            nrow = row
            ncol = col+1
        elif i=='U':
            nrow = row+1
            ncol = col
        else:
            nrow = row-1
            ncol = col

        if nrow in range(-5,6) and ncol in range(-5,6): # 범위 내에 있는 경우
            if [row,col,nrow,ncol] not in paths:
                paths.append([row,col,nrow,ncol])
                paths.append([nrow,ncol,row,col])
                answer += 1
            row,col = nrow,ncol
        else:
            nrow,ncol = row,col
    return answer

### 5 [1차] 다트 게임
## 점수|보너스|[옵션]"으로 이루어진 문자열 3세트
## 입출력 예  1S2D*3T->37 (11 * 2 + 22 * 2 + 33)
def solution(dartResult):
    answer = 0
    dart = [] #3개의 점수가 들어갈 리스트
    bonus = {"S":1, "D":2, "T":3}
    dis=[0] #3번의 기회 구별할 인덱스
    for i in range(1, len(dartResult)): #3번의 기회 구별하기 위한 숫자 찾기
        if dartResult[i].isdigit() and dartResult[i-1]!= '1':
            dis.append(i)
    dis.append(len(dartResult))

    for i in range(len(dis)-1):
        one = dartResult[dis[i]:dis[i+1]] #한번의 다트 문자열
        
        for j in range(len(one)): #보너스(S,D,T)의 위치 찾기
            if not one[j].isdigit():
                le = j
                break

        if len(one) == j+1: #옵션 없는 경우
            dart.append([int(one[:le])**bonus[one[le:le+1]]]) #계산된 점수
        else:
            dart.append([int(one[:le])**bonus[one[le:le+1]], one[le+1:]]) #계산된 점수와 옵션
    #[[1], [4, '*'], [27]]

    if '*' in dart[0]: #처음에 * 있는 경우
        dart[0] = [dart[0][0]*2]
    
    for i in [0,1,2]: #계산 과정
        if len(dart[i])==2:
            if dart[i][1] == '#':
                dart[i][0] = -dart[i][0]
            else:
                dart[i][0] = 2*dart[i][0]
                dart[i-1][0] = 2*dart[i-1][0]
                
    answer = sum(dart[i][0] for i in [0,1,2])
    return answer