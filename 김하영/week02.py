### 1 콜라츠 추측
##1-1. 입력된 수가 짝수라면 2로 나눕니다. 
##1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
##2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
## 입출력 예  6->8 / 16->4 / 626331->-1
def solution(num):
    answer = 0
    while num!=1 and answer<500:
        if num%2==0:
            num /= 2
        else:
            num = num*3+1
        answer += 1
    if answer ==500:
        answer = -1
    return answer


### 2 최솟값 만들기
## A,B에서 하나씩 골라서 곱한 후 더한 값이 최소가 되도록
## 입출력 예  [1, 4, 2], [5, 4, 4] -> 29 / [1,2], [3,4] -> 10
def solution(A,B):
    a = sorted(A)
    b = sorted(B)
    answer = sum(a[i]*b[-(i+1)] for i in range(len(A)))
    return answer
   
#     #시간초과
#     from itertools import permutations
#     answer = 0
#     answers = []
#     order = list(permutations(list(i for i in range(len(A))), len(A)))  
#     multi = list([i*j for i in A] for j in B)
    
#     for i in range(len(order)):
#         value = sum(multi[j][order[i][j]] for j in range(len(A)))
#         answers.append(value)
#     answer = min(answers)


### 3 최대공약수와 최소공배수
## 입출력 예  3,12 -> [3, 12] / 2,5 -> [1, 10]
def solution(n, m):
    #최대공약수
    max = 0
    for i in range(1, n+1 if n<m else m+1):
        if n%i==0 and m%i==0:
            max = i
    #최소공배수
    min=0
    for i in range(n*m, 0, -1):
        if i%n==0 and i%m==0:
            min = i
    answer = [max, min]
    
    # 수학 이용
    # a, b = max(n,m), min(n,m)
    # while b:
    #     a, b = b, a%b
    # answer = [a, int(n*m/a)]
    return answer

### 4 최댓값과 최솟값
## 입출력 예  "1 2 3 4" -> "1 4" / "-1 -2 -3 -4" -> "-4 -1" / "-1 -1" -> "-1 -1"
def solution(s):
    answer = ''
    numbers = s.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    #numbers = list(map(int, s.split())) #위 세줄 줄이는 방법
    numbers.sort()
    answer = str(numbers[0]) + ' ' + str(numbers[-1])
    return answer

### 5 짝수와 홀수
## 입출력 예  3 -> "Odd" / 4 -> "Even"
def solution(num):
    answer = 'Odd' if num%2 else 'Even'
    return answer

### 6 제일 작은 수 제거하기
## 입출력 예  [4,3,2,1] -> [4,3,2] / [10] -> [-1]
def solution(arr):
    answer = arr
    if len(arr) == 1:
        answer = [-1]
    else:
        min = arr[0]
        for i in answer:
            if i < min:
                min = i
        answer.remove(min)
    return answer

### 7 정수 제곱근 판별
## n이 양의 정수 x의 제곱이라면 x+1의 제곱을, 아니라면 -1 리턴
## 입출력 예  121 -> 144 / 3 -> -1
def solution(n):
    for i in range(1, n+1):
        if i*i == n:
            return (i+1)*(i+1)
    return -1

### 8 정수 내림차순으로 배치하기
## 입출력 예  118372 -> 873211
def solution(n):
    num_str = str(n)
    num_list = []
    
    for num in num_str:
        num_list.append(int(num))
    num_list.sort(reverse=True)
    
    num_str = ''
    for num in num_list:
        num_str += str(num)
    
    answer = int(num_str)

    # 줄이는 방법
    # num_list = list(str(n))
    # num_list.sort(reverse=True)
    # answer = int(''.join(num_list))
    return answer

### 9 자연수 뒤집어 배열로 만들기
## 입출력 예  12345 -> [5,4,3,2,1]
def solution(n):
    answer = list(map(int, reversed([i for i in str(n)])))
    #answer = list(map(int, reversed(str(n)))) # 줄이는 방법
    return answer

### 10 자릿수 더하기
## 입출력 예  123->6 / 987->24
def solution(n):
    str_num = str(n)
    answer = 0
    for i in str_num:
        answer += int(i)
    #answer = sum([int(i) for i in str(number)])
    return answer