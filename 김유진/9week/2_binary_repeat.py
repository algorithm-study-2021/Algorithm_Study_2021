#SRP 원리 준수 

def detectZero(s): #count 써도 됨
    #0의 개수 반환
    count=0
    for i in s:
        if i=="0": count+=1

    return count

def removeZero(s):
    #반환: 0 제거된 문자열
    str=""
    for i in s:
        if i!="0": str+=i
    
    return str

def solution(s):
    cnt=0
    zeros=0
    while s!="1":
        removes=detectZero(s);zeros+=removes
        s=removeZero(s) #현재 s는 0 제거됨
        length=len(s) #제거 후 길이

        #s-> lenth의 2진수 변환 문자열로 
        s=format(length,'b')
        cnt+=1

    return [cnt,zeros]

print(solution("110010101001"))