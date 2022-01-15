#3>30 
#사전순에서, 길이문제 
def solution(numbers):
    #모두 0이면 "0" 반환 -> case 11
    zero=True
    for i in numbers:
        if i!=0: zero=False; break
    if zero==True: return "0"

    res=""
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])

    #뒤에 붙이는 것보다 *3이 효율적
    numbers.sort(key=lambda x:x*3,reverse=True) #str은 -로 reverse 불가

    for i in numbers:
        res+=i
    
    return res