def solution(x):
    ex=x #원래 값을 유지하기 위해 ex에 복사
    num=1 #자릿수-1
    while ex>=10:
        ex/=10
        num+=1
    a=[] #모든 자릿수 분리
    ex=x
    for i in range(num):
        a.append(ex%10)
        ex//=10
    sum=0 #모든 자릿수의 합
    for j in range(len(a)):
        sum+=a[j]
    
    if x%sum==0:
        answer=True
    elif x%sum!=0:
        answer=False
        
    return answer
