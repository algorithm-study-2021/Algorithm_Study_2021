"""
지속적인 오류:  must be str, not int
문자열에 정수 더하는 경우 생김
list(s) 한다고 문자열의 요소가 chr로 고려되지 않음, 여전히 str (type 함수로 확인 )

+int형으로 변경할 때 (int)i 가 아니라 int(i)임 

추가적인 오류: ValueError- invalid literal for int() with base 10 (str 오류)
"""
def upperMethod(s):
    res=""
    for i in list(s):
        if i<'a': #Capital case
            #upeer로 변환
            temp_i=ord(i)+32
            res+=chr(temp_i)
        else: res+=i
    return res

def rmFactor(arr, factor):
    res=[]
    for i in arr:
        if i!=factor:
            res.append(i)
    return res

def solution(cacheSize, cities):

    if cacheSize==0:
        return len(cities)*5
    cache=[] 
    time=0
    for i in cities:
        i=upperMethod(i) 

        #cache hit(1)
        if i in cache: #O(n)
            cache=rmFactor(cache,i)
            cache.append(i)
            time+=1

        #cache miss(5)
        else: 
            if len(cache)==cacheSize: #cache full
                cache.pop(0) 
                cache.append(i)
                time+=5

            else: 
                cache.append(i)
                time+=5
    return time

print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))