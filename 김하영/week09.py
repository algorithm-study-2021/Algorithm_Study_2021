### 1 2016년
## 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일
## 입출력 예  5,24 -> "TUE"
def solution(a, b):
    months=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=['THU','FRI','SAT','SUN','MON','TUE','WED']
    day=0
    for i in range(a-1):
        day += months[i]
    day += b
    return days[day%7]

### 2 영어 끝말잇기
## 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 
## 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
## 입출력 예  3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]->[3,3]
def solution(n, words):
    answer = []
    index=0
    past=[words[0]] #첫단어 미리 넣어주기
    for i in range(1, len(words)): #탈락 단어 찾기
        if words[i][0] != words[i-1][-1]: #틀린 끝말잇기
            index=i
            break
        if words[i] not in past: #성공 단어
            past.append(words[i])
        else: #나왔던 단어
            index=i
            break
    if index==0: #탈락자 없는
        answer = [0,0]
    else:
        if (index+1)%n==0: #0번째가 없으므로 n번째로
            answer.append(n)
        else:
            answer.append((index+1)%n)
        answer.append(index//n+1)
    return answer

### 3 삼각 달팽이
## 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행
## 입출력 예  6-> [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
def solution(n):
    answer = []
    matrix = [[0 for i in range(n)] for j in range(n)]
    row = -1 #시작점 변수
    col = 0
    number = 1
    for i in range(n):
        if i%3==0: #밑으로 증가
            for j in range(n-i):
                row += 1
                matrix[row][col] = number
                number += 1
        elif i%3==1: #옆으로 증가
            for j in range(n-i):
                col += 1
                matrix[row][col] = number
                number += 1
        else: #대각선으로 증가
            for j in range(n-i):
                row-=1
                col-=1
                matrix[row][col] = number
                number += 1
    for i in range(len(matrix)): #리스트로 옮기기
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                answer.append(matrix[i][j])
            else:
                break
    return answer
