### 1 문자열 내 p와 y의 개수
## 'p'의 개수와 'y'의 개수를 비교해 같으면 True
## 입출력 예  "pPoooyY" -> true / "Pyy" -> false
def solution(s):
    pnum=0
    ynum=0
    for i in s:
        if i=="p" or i=="P":
            pnum += 1
        elif i=="y" or i=="Y":
            ynum += 1
    answer = True if pnum==ynum else False
    return answer
#answer = s.lower().count('p') == s.lower().count('y')

### 2 문자열 내 마음대로 정렬하기
## 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
## 입출력 예  ["abce", "abcd", "cdx"], 2 -> ["abcd", "abce", "cdx"]
def solution(strings, n):
    letters = list(map(list, strings))
    letters.sort(key=lambda x:(x[n],x)) #글자순 후 사전순
    answer = list(map(''.join,letters))
    return answer
#answer = sorted(strings, key=lambda x:(x[n], x))

### 3 땅따먹기
## 한 행에 한 칸의 땅을 밟으며 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없다. 최고점?
## 입출력 예  [[1,2,3,5],[5,6,7,8],[4,3,2,1]] -> 16
def solution(land):
    matrix = [[0 for col in range(4)] for row in range(len(land)-1)] # 누적된 값이 저장될 행렬
    matrix.insert(0, [land[0][i] for i in range(4)]) #첫번째 행 입력
    for i in range(len(land)-1):
        curMax = max(matrix[i]) #누적된 값들 중 가장 큰 수
        curIn = matrix[i].index(curMax) # curMax의 위치(열)
        second = sorted(matrix[i])[-2] # 누적된 현재 줄에서 두번째로 큰 수
        temp = land[i+1][curIn] + second #matrix에서 가장 큰 수 아래로 들어갈 값
        for j in range(4): # 최대 누적 수를 다음 행에 더함
            matrix[i+1][j] = land[i+1][j] + curMax
        matrix[i+1][curIn] = temp
    answer = max(matrix[-1])
    return answer

### 4 두 정수 사이의 합
## a와 b 사이에 속한 모든 정수의 합
## 입출력 예  3,5 -> 12 / 3,3 -> 3 / 5,3 -> 12
def solution(a, b):
    answer = sum(range(a, b+1)) if a<b else sum(range(b, a+1))
    return answer

### 5 다음 큰 숫자
## n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
## 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)
## 입출력 예  78 -> 83 / 15 -> 23
def solution(n):
    answer = n+1
    num1 = numOfOne(n)
    while True:
        if num1 == numOfOne(answer):
            break
        answer += 1
    return answer

def numOfOne(n):
    binary = ''
    while n>0: #이진수로 변환
        binary = str(n%2) + binary
        n = int(n/2)
    return binary.count('1')

### 6 나누어 떨어지는 숫자 배열
## 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환, 없다면 배열에 -1을 반환
## 입출력 예  [5, 9, 7, 10], 5 -> [5, 10] / [3,2,6], 10 -> [-1]
def solution(arr, divisor):
    arr.sort()
    answer = [i for i in arr if i%divisor==0]
    if answer == []:
        answer = [-1]
    return answer

### 7 [3차] n진수 게임
## 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 
## 입출력 예  2,4,2,1 -> "0111" / 16,16,2,2 -> "13579BDF01234567"
def solution(n, t, m, p):
    answer = ''
    numbers = ['0'] # 숫자 순서
    num10 = 1 # 10진수
    while True:
        changed = changenum(n, num10)
        for i in changed: # 문자열 하나씩으로 분리
            numbers.append(i)
        if len(numbers) >= t*m:
            break
        num10 += 1
        
    for i in range(p-1, t*m, m): # 튜브의 순서
        answer += numbers[i]  
    return answer

def changenum(n, num): # 진수 변환 함수
    answer=''
    while num!= 0:
        remainder = num%n
        if 9 < remainder <16: #65가 A
            answer = chr(remainder+55) + answer
        else:
            answer = str(num%n) + answer
        num = int(num/n)
    return answer

### 8 올바른 괄호
## '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다
## 입출력 예  "(())()"->true / ")()("->false
def solution(s):
    check = 0
    for i in s:
        if i == '(':
            check += 1
        else:
            check -= 1
        if check<0: #')'가 '('보다 먼저 나오는 경우
            break
    return True if check==0 else False

### 9 [3차] 파일명 정렬
## 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로
## 입출력 예  
##입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
##출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
def solution(files):
    answer = []
    divided = []
    numbers='0123456789'
    for file in files:
        d1, d2 = 0, 0
        for i in range(len(file)):
            if file[i] in numbers:
                d1=i #number의 시작
                break
        for i in range(d1+1, len(file)):
            if file[i] not in numbers:
                d2=i #tail의 시작
                break
        if d2==0:
            d2 = len(file)
        divided.append([file[:d1].lower(), int(file[d1:d2]),files.index(file)])
    divided.sort(key=lambda x:(x[0], x[1]))

    for i in range(len(files)):
        answer.append(files[divided[i][2]])
    return answer

### 10 같은 숫자는 싫어
## 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거 / 순서를 유지
## 입출력 예  [1,1,3,3,0,1,1] -> [1,3,0,1] / [4,4,4,3,3]->[4,3]
def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
# a[-1:]은 마지막 값 담은 리스트 / 빈 리스트면 빈 리스트 반환