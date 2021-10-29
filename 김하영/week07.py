### 1 점프와 순간 이동
## 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동
## 입출력 예  5->2 / 6->2 / 5000->5
def solution(n):
    #2의 제곱이 몇개인가
    ans=0
    while n>0:
        num=1
        while num*2 <= n:
            num *= 2
        n -= num
        ans += 1
    return ans

### 2 이진 변환 반복하기
## x = "0111010" -> "1111"(0 제거) -> "100"(길이 2진법으로)
## 1 될때까지 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수
## 입출력 예  "110010101001"->[3,8] / "01110"->[3,3]
def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += s.count('0')
        c = s.count('1')
        s = ''
        while c>0:
            s = s + str(c%2)
            c = c//2
        answer[0] += 1
    return answer

### 3 나머지가 1이 되는 수 찾기
## n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return
## 입출력 예  10->3 / 12->11
def solution(n):
    answer = 0
    for i in range(2,n):
        if (n-1) % i == 0:
            answer = i
            break
    return answer

### 4 [1차] 캐시
## 캐시 교체 알고리즘은 LRU / cache hit일 경우 실행시간은 1, miss는 5
## 입출력 예  3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]->50
## 입출력 예  3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]->21
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in range(len(cities)): #cache에 있는지 확인
        if cities[i].lower() not in cache:
            answer += 5
        else:
            cache.remove(cities[i].lower())
            answer += 1
        cache.append(cities[i].lower()) #뒤에 추가
        
        if len(cache) > cacheSize:
            del cache[0]
    return answer

### 5 5주차_모음사전
## 'A', 'E', 'I', 'O', 'U'만을 사용 / 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"
## 입출력 예  "AAAAE"->6 / "AAAE"->10 / "I"->1563 / "EIO"->1189
def solution(word):
    answer = 0
    ltonum = {'A':'0', 'E':'1', 'I':'2', 'O':'3', 'U':'4', 'X':'X'}
    mul = [781,156,31,6,1] #자릿수 별 한 문자가 갖는 갯수
    if len(word) != 5: #X로 채워 5자리로
        word = word+ 'X'*(5-len(word))
    
    wordtonum = ''
    for i in word: #문자를 숫자로
        wordtonum += ltonum[i]
    print(wordtonum)
    
    for i in range(len(wordtonum)):
        if wordtonum[i] != 'X':
            answer = answer + (mul[i]*int(wordtonum[i])+1)
    
    return answer