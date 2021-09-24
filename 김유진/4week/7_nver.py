#리팩토링 시행 (SRP)
#진수 구하는 함수 (nVer 코드만 훔침 ㅠ )
def nVer(num,n):
    arr="0123456789ABCDEF"
    ret=''
    if num==0:
        return '0'
    while num>0:
        ret=arr[num%n]+ret #뒤에부터 더해줌 
        num=num//n 
    return ret 


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

    return returnString

print(solution(16,16,2,1))