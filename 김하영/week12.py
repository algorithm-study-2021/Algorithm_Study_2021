### 1 두 개 뽑아서 더하기
## 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로
## 입출력 예  [2,1,3,4,1]->[2,3,4,5,6,7]
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                 answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer

### 2 괄호 회전하기
## s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수
## 입출력 예  "[](){}"->3 / "[)(]"->0
def solution(s):
    answer = 0
    for i in range(len(s)):
        se = s[i:] + s[:i]
        if checkorder(se) == True:
            answer += 1
    return answer

def checkorder(s):
    check = True
    isopen = {'[':True, '{':True, '(':True, ']':False, '}':False, ')':False}
    bracket = {'[':0, ']':0, '{':1, '}':1, '(':2, ')':2}
    order = [] #괄호 종류 담는 리스트 / 0,1,2로
    each = [0,0,0] #괄호별 체크(대, 중, 소)
    for i in range(len(s)):
        if isopen[s[i]]: #열리는 괄호
            each[bracket[s[i]]] += 1
            order.append(bracket[s[i]])
        else: #닫히는 괄호
            each[bracket[s[i]]] -= 1
            if len(order)!=0:
                if order[-1] != bracket[s[i]]: #괄호 순서를 위해
                    check = False 
                else:
                    del order[-1]
        if -1 in each: #닫히는 괄호가 먼저 나온 경우
            check = False
        if check==False:
            break
    for i in each: #열린 괄호 존재하는 경우
        if i != 0:
            check=False
    return check

### 3 후보키
## 릴레이션에서 후보 키의 개수
