#!/usr/bin/env python
# coding: utf-8

# ## 1. 직사각형 별찍기
# #### 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
# 
# #### 제한 조건
# n과 m은 각각 1000 이하인 자연수입니다.
# 
# 
# #### 예시 입력
# 
# ```
# 5 3
# ```
# 
# #### 출력
# ```
# *****
# *****
# *****
# ```

# In[15]:


a, b = map(int, input().split(' '))
for j in range(0, b):
    for i in range(0, a):
        print("*", end = '')
    print()


# ## 2. x만큼 간격이 있는 n개의 숫자
# 
# #### 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.
# 
# #### 입출력 예
# ```
# x	n	answer
# 2	5	[2,4,6,8,10]
# 4	3	[4,8,12]
# -4	2	[-4, -8]
# ```

# In[27]:


def solution(x, n):
    answer = []
    z = 0
    for i in range(0, n):
        z = z + x
        answer.append(z)
        n = n + 1
    return answer

x, n = map(int, input().split(' '))
solution(x, n)


# ## 3. N개의 최소공배수
# 
# #### 문제 설명
# 
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# 
# #### 제한 사항
# 
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 
# #### 입출력 예
# ```
#    arr	     result
# [2,6,8,14]	  168
# [1,2,3]	6
# ```

# In[46]:


from math import gcd

def solution(arr):
    
    def lcm(x, y):
        return x * y // gcd(x,y)
    
    while(1):
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
        
print(solution(arr))

arr = input().split(' ')
arr = list(map(int, arr))


# #### 1.
# 
# 파이썬 내장함수 gcd()를 이용한 lcm()에서 arr의 요소 두개를 pop()하여 최소공배수를 구한다. 구한 최소공배수는 arr로 다시 삽입한다.

# ## 4. JadenCase 문자열 만들기
# 
# #### 문제 설명
# 
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# 
# s는 길이 1 이상인 문자열입니다.
# s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
# 
# #### 입출력 예
# 
# ```
#           s	                   return
#           
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"
# ```

# In[44]:


def solution(s):
    s = s.split(' ')
    for i in range(0, len(s)):
        s[i] = s[i].capitalize()
    answer = (" ".join(map(str, s)))
    return answer

solution('3people unFollowed me')


# #### 1.
# s.split()으로 쓰면 공백이 여러개여도 하나로 취급되기때문에 통과를 못했던 것...! 
# 공백이 여러개일 때도 분리시켜야하므로 s.split(' ')으로 쓰자
# 
# #### 2.
# 파이썬에서 str목록을 문자열로 변환할 때 '" ".join(map(str, s))'와 같이 나타낸다.
# map함수는 str함수를 목록 s의 모든 항목에 적용하고 map 객체를 반환한다. "".join()은 map객체의 모든 요소를 반복하고 연결된 요소를 문자열로 반환한다.

# ## 5. 행렬의 덧셈
# 
# #### 문제 설명
# 
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# 
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 
# #### 입출력 예
# ```
# arr1	             arr2	        return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	       [[3],[4]]	[[4],[6]]
# ```

# In[12]:


arr1 = [[1],[2]]
arr2 = [[3],[4]]

answer = []

for i in range (0, len(arr1)):
    temp = []
    for j in range (0, len(arr1[0])):
        temp.append(arr1[i][j]+arr2[i][j])
    answer.append(temp)
print(answer)

"""
def solution(arr1, arr2):
    answer = []
    for i in range (0, len(arr1)):
        temp = []
        for j in range (0, len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer
"""


# ## 6. 행렬의 곱셈
# 
# #### 문제 설명
# 
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# 
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.
# 
# #### 입출력 예
# 
# ```
#           arr1	                  arr2	              return
# [[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
# [[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
# ```

# In[4]:


import numpy as np

def solution(A, B):
    answer = np.dot(A, B).tolist()
    return answer

"""
def solution(A, B):
    n = len(A)
    if n == 1:
        return A * B
    
    n2 = n//2
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:]
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:]
    
    M1 = solution(A11+A22, B11+B22)
    M2 = solution(A21+A22, B11)
    M3 = solution(A11, B12-B22)
    M4 = solution(A22, B21-B11)
    M5 = solution(A11+A12, B22)
    M6 = solution(A21-A11, B11+B12)
    M7 = solution(A12-A22, B21+B22)
    
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    return C
A = np.array([[0,1],[2,3]])
B = np.array([[4,5],[0,2]])
C = solution(A, B)
print(C)
"""

"""
import numpy as np

def solution(A, B):
    
    A = np.array(A)
    B = np.array(B)
    
    n = len(A)
    if n == 1:
        return A * B
    
    n2 = n//2
    A11, A12, A21, A22 = A[:n2, :n2], A[:n2, n2:], A[n2:, :n2], A[n2:, n2:]
    B11, B12, B21, B22 = B[:n2, :n2], B[:n2, n2:], B[n2:, :n2], B[n2:, n2:]
    
    M1 = solution(A11+A22, B11+B22)
    M2 = solution(A21+A22, B11)
    M3 = solution(A11, B12-B22)
    M4 = solution(A22, B21-B11)
    M5 = solution(A11+A12, B22)
    M6 = solution(A21-A11, B11+B12)
    M7 = solution(A12-A22, B21+B22)
    
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))).tolist()
    
    return C

"""

"""
def solution(arr1, arr2):
    answer = [[0 for _ in range(0, len(arr2[0]))] for _ in range(0, len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] = answer[i][j] + (arr1[i][k] * arr2[k][j])
    return answer

arr1 = [[1,0],[0,1]]
arr2 = [[3,2],[4,5]]

print(solution(arr1, arr2))
"""


# ### 쉬트라센 알고리즘
# 
# 쉬트라센 방법은 행렬을 4개의 부분 행렬로 분할한다. n * n 행렬은 네 개의 n / 2 * n / 2 행렬 A11, A12, A21, A22(B행렬도 마찬가지)로 나눌 수 있다.
# 
# ![image.png](attachment:image.png)
# 
# 쉬트라센 알고리즘에 따라 다음 7개의 수식으로 C를 표현할 수 있다.
# 
# ![image.png](attachment:image.png)
# 
# 
# ### 단순 알고리즘
# 
# answer를 for문을 통한 반복문으로 결과 행렬만큼 0으로 초기화해준다.
# 
# 행렬 곱의 원리를 적용해서 삼중 for문을 만들얻 초기화했던 answer에 값을 더해준다.

# ## 7. 핸드폰 번호 가리기
# 
# #### 문제 설명
# 
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# 
# s는 길이 4 이상, 20이하인 문자열입니다.
# 
# #### 입출력 예
# 
# ```
# phone_number	   return
# "01033334444"	"*******4444"
# "027778888"	    "*****8888"
# ```

# In[23]:


def solution(phone_number):
    answer = ''
    for _ in range(len(phone_number)-4):
        answer += '*'
    answer += phone_number[len(phone_number)-4:]
    return answer

solution('01098567975')


# ## 8. 하샤드 수
# 
# #### 문제 설명
# 
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
# 
# #### 제한 조건
# 
# x는 1 이상, 10000 이하인 정수입니다.
# 
# #### 입출력 예
# ```
# arr	return
# 10	true
# 12	true
# 11	false
# 13	false
# ```
# 
# #### 입출력 예 설명
# 
# 입출력 예1
# 10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.
# 
# 입출력 예2
# 12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.
# 
# 입출력 예3
# 11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.
# 
# 입출력 예4
# 13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

# In[14]:


def solution(x):
    sum = 0
    tx = x
    while(x>=10):
        sum += x % 10
        x = x // 10
    sum += x
    if(tx % sum == 0):
        answer = True
    else:
        answer = False
    return answer

x = int(input())
solution(x)


# ## 9. 피보나치 수
# 
# #### 문제 설명
# 
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# 
# 예를들어
# 
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.
# 
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# 
# #### 제한 사항
# 
# * n은 1이상, 100000이하인 자연수입니다.
# 
# #### 입출력 예
# ```
# n	return
# 3	2
# 5	5
# ```
# #### 입출력 예 설명
# 
# 피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.

# In[28]:


def solution(n):
    fi, se = 0, 1
    for _ in range (n-1):
        fi, se = se, fi + se 
    return se % 1234567

solution(2)


# 입력예시에 n이 100000까지 인데 왜 1234567로 나누라고 한지 모르겠다..
# 
# 처음엔 if-else를 활용한 재귀함수를 사용해서 풀었는데 런타임 에러가 나서 반복문으로 fi와 se의 자리를 왼쪽으로 한칸 씩 미는 방식으로 풀었다.

# ## 10. 평균 구하기
# 
# #### 문제 설명
# 
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# 
# #### 제한사항
# 
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
# 
# #### 입출력 예
# ```
#    arr	   return
# [1,2,3,4]	2.5
# [5,5]	     5
# ```

# In[39]:


def solution(arr):
    arr = list(map(int, arr))
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    answer = answer / len(arr)
    return answer

arr = [1,2,3,4]
print(solution(arr))


# sum 함수를 사용하자!
# 
# ```
# return (sum(list) / len(list))
# ```

# In[ ]:




