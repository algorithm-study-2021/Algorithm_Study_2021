### 1 이상한 문자 만들기
## 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로
## 입출력 예  "try hello world"->"TrY HeLlO WoRlD"
def solution(s):
    letter = 0 #단어 내에서 몇번째 글자인지 확인하기 위한 변수
    answer = ''
    for i in range(len(s)):
        if s[i]== ' ':
            answer += ' '
            letter=0
        else:
            answer = answer+s[i].upper() if letter%2==0 else answer+s[i].lower()
            letter += 1
    return answer

### 2 약수의 합
## 입출력 예  12->28 / 5->6
def solution(n):
    ##0.15ms/10.2mb
    # answer = 0
    # divisors = []
    # for i in range(1, n+1):
    #     if n%i==0:
    #         divisors.append(i)
    # answer = sum(divisors)
    ##위를 줄인 것
    answer = sum(number for number in range(1, n+1) if n%number==0)
    return answer
## 더 효율적으로
#answer = n+ sum(number for number in range(1, int(n/2)+1) if n%number==0) #0.07ms

### 3 시저 암호 *
## 입출력 예  "AB",1 -> "BC" / "z",1 -> "a" / "a B z",4 -> "e F d"
def solution(s, n):
    letters = list(s)
    for i in range(len(s)):
        if 'A' <= letters[i] <= 'Z': # A=65
            letters[i] = chr(((ord(s[i]))-65+n)%26 + 65)
        elif 'a' <= letters[i] <= 'z': # a=97
            letters[i] = chr(((ord(s[i]))-97+n)%26 + 97)
    answer = ''.join(letters)
    return answer

### 4 문자열을 정수로 바꾸기
## 입출력 예  "1234" -> 1234 / "-1234" -> -1234
def solution(s):
    answer = 0
    if s[0] == '-' or s[0] == '+':
        answer = int(s[1:])
    else : 
        answer = int(s)
    if s[0]=='-':
        answer = -answer
    return answer
#answer = int(s) # 부호 알아서 인식해줌

### 5 숫자의 표현
## 연속된 자연수들로 n을 표현하는 방법의 수 (15=1+2+3+4+5=4+5+6=7+8)
## 입출력 예  15 -> 4
def solution(n):
    answer = 1 # 본인으로 인한 기본값
    for i in range(1, int(n/2)+1): # 시작 숫자
        value=0 # 덧셈으로 누적될 값
        for j in range(i,int(n/2)+2):
            value += j
            if value >= n:
                break
        if value == n:
            answer += 1
    return answer

### 6 수박수박수박수박수박수?
## 입출력 예  3 -> "수박수" / 4 -> "수박수박"
def solution(n):
    answer = '수박'*(n//2) if n%2==0 else '수박'*int(n/2)+'수'
    return answer
#answer = "수박"*(n//2) + "수"*(n%2)


### 7 소수 찾기 *
## 입출력 예  10 -> 4 / 5 -> 3
def solution(n):
    num_set = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num_set: # 배수 제거
            num_set -= set(range(i*2, n+1, i))

    answer = len(num_set)
    return answer

# #시간 초과
# def solution2(n):
#     answer = 0
#     primes = [2]
#     for number in range(2, n+1):
#         check=True
#         for j in primes:
#             if number%j==0:
#                 check=False
#                 break
#         if check==True:
#             primes.append(number)
#     answer = len(primes)
#     return answer
# #시간 초과
# def solution1(n):
#     answer = 0
#     for number in range(2, n+1):
#         check=True
#         for j in range(2, int(number/2)+1):
#             if number%j==0:
#                 check=False
#                 break
#         if check==True:
#             answer += 1
#     return answer


### 8 서울에서 김서방 찾기
## 입출력 예  ["Jane", "Kim"]->"김서방은 1에 있다"
def solution(seoul):
    answer = "김서방은 " + str(list(i for i in range(len(seoul)) if seoul[i]=="Kim")[0]) +"에 있다"
    return answer
    #answer = "김서방은 {}에 있다".format(seoul.index('Kim'))

### 9 문자열 다루기 기본
## 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
## 입출력 예  "a234" -> false / "1234" -> true
def solution(s):
    answer = True if len(s) == 4 or len(s) == 6 else False
    for i in s:
        if not(47 < ord(i) < 58):
            answer = False
    return answer
    # answer = s.isdigit() and len(s) in (4, 6)

### 10 문자열 내림차순으로 배치하기
## 입출력 예  "Zbcdefg" -> "gfedcbZ"
def solution(s):
    letters = list(s)
    letters.sort(reverse=True)
    answer = ''.join(letters)
    return answer