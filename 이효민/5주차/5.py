def solution(dartResult):
    answer = 0
    
    dartResult=list(dartResult)
    a=len(dartResult)
    num=[]
    for i in range(0,a):
        if dartResult[i].isdigit():
            if dartResult[i+1].isdigit():
                num.append(int(dartResult[i]+dartResult[i+1]))
                dartResult[i+1]="."
            else:
                num.append(int(dartResult[i]))
        elif dartResult[i]=="S":
            continue
        elif dartResult[i]=="D":
            num[len(num)-1]=num[len(num)-1]**2
        elif dartResult[i]=="T":
            num[len(num)-1]=num[len(num)-1]**3
        elif dartResult[i]=="*":
            num[len(num)-1]*=2
            if len(num)!=1:
                num[len(num)-2]*=2
        elif dartResult[i]=="#":
            num[len(num)-1]*=-1
    
    print(num)
    answer=sum(num)
    
    return answer
