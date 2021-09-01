### 1 직사각형 별찍기
n, m = map(int, input().split())
print((('*'*n+'\n')*m).rstrip())

### 2 x만큼 간격이 있는 n개의 숫자
## 입출력 예  x = -4, n = 2 -> [-4, -8] / x = 4, n = 3 -> [4,8,12]
def solution(x, n):
    answer = [x+x*i for i in range(n)]
    return answer

### 3 N개의 최소공배수
def solution(arr): 
    answer = 1
    for i in range(len(arr)):
        temp = 1
        for j in range(answer*arr[i], 0, -1): # 큰수부터 작은수 차례로
            if j%answer==0 and j%arr[i]==0:
                temp = j
        answer = temp
    return answer
## 내장함수 이용
# from math import gcd
# answer = arr[0]
# for num in arr:
#     answer = answer*num // gcd(answer, num)

### 4 JadenCase 문자열 만들기
## 입출력 예  "3people unFollowed me" -> "3people Unfollowed Me"
def solution(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()    
    return answer

### 5 행렬의 덧셈
## 입출력 예  arr1 = [[1,2],[2,3]], arr2 = [[3,4],[5,6]] -> [[4,6],[7,9]]
def solution(arr1, arr2):
    #answer = [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] += arr2[i][j]
    return answer

### 6 행렬의 곱셈
## 입출력 예  arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]] -> [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
def solution(arr1, arr2):
    # answer = [[sum(a*b for a, b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1] 
    #*은 unpack으로 리스트를 풀어줌
    answer=[]
    value=0
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            value = 0
            for k in range(len(arr1[i])):
                value += arr1[i][k]*arr2[k][j]
            temp.append(value)
        answer.append(temp)
    return answer

### 7 핸드폰 번호 가리기
## 입출력 예  "01033334444" -> "*******4444" / "027778888" -> "*****8888"
def solution(phone_number):
    answer = '*'*(len(phone_number)-4)+phone_number[-4:]
    return answer

### 8 하샤드 수
## 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
## 입출력 예  10 -> true / 12 -> true / 11 -> false / 13 -> false
def solution(x):
    #answer = x%sum([int(a) for a in str(x)]) == 0
    val = 0
    for i in range(len(str(x))):
        val += int(str(x)[i])
    answer = True if (x % val) == 0 else False
    return answer

### 9 피보나치 수
## 입출력 예  3 -> 2 / 5 -> 5
def solution(n):
    answer = 0
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])
    answer = fib[-1] % 1234567
    return answer

### 10 평균 구하기
## 입출력 예  [1,2,3,4] -> 2.5 / [5,5] -> 5
def solution(arr):
    answer = sum(arr) / len(arr)
    return answer