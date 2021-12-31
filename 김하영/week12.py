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
import itertools

def solution(relation):
    combi = [] #항목 모든 조합
    include = False
    for i in range(1, len(relation[0])+1):
        combi = combi + list(itertools.combinations(range(0,len(relation[0])),i))

    keys = [] # 후보키 리스트
    for i in range(len(combi)):
        if len(keys) != 0:
            for k in keys: #최소성 점검
                include = True
                for n in range(len(k)):
                    if k[n] not in combi[i]:
                        include = False
                        break
                if include == True:
                    break
        if include == True: #최소성 만족하지 않는 경우
            continue #다음 combi[i]로
        iskey = True
        temp = []
        for row in range(len(relation)):
            student = [] #항목 뽑아낸 한줄 리스트
            for c in combi[i]:
                student.append(relation[row][c])
            if student not in temp: 
                temp.append(student)
            else: #중복되는 값 있는 경우
                iskey = False
                break
        if iskey == True:
            keys.append(combi[i])

    answer = len(keys)

    return answer

## 효율성 실패
### 4 순위 검색
## 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return
def solution(info, query):
    answer = [0 for i in range(len(query))]
    infos = [] # info 문장을 리스트로 나눠서
    for i in range(len(info)):
        infos.append(info[i].split())
    
    for i in range(len(query)):
        #query를 배열로
        querylist = query[i].split()
        for q in range(len(querylist)-1,-1,-1): #and 빼기
            if querylist[q] == 'and':
                del querylist[q]
        
        for j in range(len(infos)): #info 하나씩 비교
            check = True
            for num in range(4):
                if querylist[num] == '-':
                    continue
                if querylist[num] != infos[j][num]:
                    check = False
                    break
            if check == True:
                if int(infos[j][4]) >= int(querylist[4]): #점수 조건
                    answer[i] += 1
            
    return answer

### 5 예상 대진표
## 몇 번째 라운드에서 만나는지
## 입출력 예  8,4,7 -> 3
def solution(n,a,b):
    answer = 0
    s = 1 #범위의 시작값
    while True:
        if location(s, n, a) != location(s, n, b):
            break
        elif location(s,n,a) == 'before': #절반씩 범위를 좁혀가는 과정
            n = n - (n-s+1)//2 #범위의 마지막 값
        else:
            s = s + (n-s+1)//2
    
    x = n-s+1 
    while x!=1: #2의 몇승인지
        x = x//2
        answer += 1
    return answer

def location(s, n, x): #중간값 전후 판별
    mid = (s+n-1)//2
    if x > mid:
        answer = 'after'
    else:
        answer = 'before'
    return answer
