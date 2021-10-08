### 1 가운데 글자 가져오기
## 입출력 예  "abcde"->"c" / "qwer"->"we"
def solution(s):
    answer = s[len(s)//2:len(s)//2+1] if len(s)%2==1 else s[len(s)//2-1:len(s)//2+1]
    return answer

### 2 스킬트리
## 가능한 스킬트리 개수를 return
## 입출력 예  "CBD", ["BACDE", "CBADF", "AECB", "BDA"]->2
def solution(skill, skill_trees):
    answer = 0
    
    for tested in skill_trees:
        slist=list(skill)
        
        for i in range(len(tested)): # 스킬 인덱스 추가
            if tested[i] in skill:
                slist[slist.index(tested[i])] = [tested[i], i]

        for i in range(len(slist)): # 없는 스킬의 인덱스 최댓값으로
            if len(slist[i])==1:
                slist[i] = [slist[i], len(skill_trees)]
        
        check = True
        for i in range(1, len(slist)):
            if slist[i-1][1] > slist[i][1]:
                check = False
                break
                
        if check==True:
            answer += 1
    
    return answer
#for-else문

### 3 쿼드압축 후 개수 세기
##  쿼드 트리와 같은 방식으로 압축 후 배열에 최종적으로 남는 0의 개수와 1의 개수
## 입출력 예  [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]->[4,9]
def solution(arr):
    answer = [0,0]
    div = 1 # 나누는 지점 설정을 위한 변수
    
    while len(arr)//div > 1:
        dots=[]
        for i in range(0,len(arr),len(arr)//div): # 나누는 지점
            for j in range(0,len(arr),len(arr)//div):
                dots.append([i,j])
        
        for i in dots:
            partsum=0
            for row in range(i[0], i[0]+len(arr)//div): #부분의 합
                for col in range(i[1], i[1]+len(arr)//div):
                    partsum += arr[row][col]
            
            if partsum == 0: #부분이 모두 0인 경우
                answer[0] += 1
                for row in range(i[0], i[0]+len(arr)//div):
                    for col in range(i[1], i[1]+len(arr)//div):
                        arr[row][col] = 2
            elif partsum == (len(arr)//div)**2: #부분이 모두 1인 경우
                answer[1] += 1
                for row in range(i[0], i[0]+len(arr)//div):
                    for col in range(i[1], i[1]+len(arr)//div):
                        arr[row][col] = 2
        div *= 2
        
    for i in arr: #남은 0과 1의 갯수 더하기
        answer[0] += i.count(0)
        answer[1] += i.count(1)
    return answer

### 4 [1차] 비밀지도
## 각 칸은 "공백"(" ") 또는 "벽"("#") / 모두 공백인 부분은 전체 지도에서도 공백으로
## 입출력 예  5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28] -> ["#####","# # #", "### #", "# ##", "#####"]
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)): #이진수로 값 변환
        arr1[i] = tobin(n,arr1[i])
    for i in range(len(arr2)):
        arr2[i] = tobin(n,arr2[i])
    
    for i in range(len(arr1)): # 전체지도
        row = ''
        for j in range(len(arr1)):
             row += ' ' if arr1[i][j]=='0' and arr2[i][j]=='0' else '#'
        answer.append(row)
    return answer

def tobin(n, num):
    bin = ''
    for i in range(n):
        bin = str(num%2) + bin
        num = num//2
    return bin

### 5 부족한 금액 계산하기
## 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배
## 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return
## 입출력 예  3, 20, 4 -> 10
def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count+1):
        total += price*i
        print(total)
    if total > money:
        answer = total-money
    else:
        answer = 0

    return answer