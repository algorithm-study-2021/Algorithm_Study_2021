#리팩토링 시행 (SRP)
def nVer(num,n):
    if n==2:
        return format(num,'b')
    elif n==8:
        return format(num,'o')
    elif n==10:
        return str(num)
    elif n==16:
        return format(num,'x')
    #여기에 try-catch 처리해주기

def solution(n, t, m, p):
    nowNum=0 #현재 숫자(10진법)
    returnString=''
    turn=1
 
    nowNum_nver=nVer(nowNum,n)

    #하나씩 비교
    while(len(returnString)!=t): #받을 거 다 받으면 종료
        #빈 문자열인 경우
        if len(nowNum_nver)==0:
            nowNum+=1
            nowNum_nver=nVer(nowNum,n)

        if(turn>m): turn=1 #turn 돌아가는 과정

        #차례
        if(turn==p):
            returnString+=nowNum_nver[0]

        #다음 차례를 위해 재정의 
        if(len(nowNum_nver))==1: nowNum_nver=''
        else: nowNum_nver=nowNum_nver[1:]
        turn+=1 

    return returnString.upper()

print(solution(16,16,2,1))

#3진법, 4진법, 등등에 대해서도 시행해줘야 함 