#큰 수 만들기
def solution(number, k):
    answer = ''
    
    rem_count=0
    number=list(number)
    for i in range(0,len(number)):
        if rem_count>=k:
            break
        number,rem_count=rem(number,rem_count,k)
        
    for j in range(1,len(number)):
        number[0]+=number[j]
    answer=number[0]
        
    return answer

def rem(number,rem_count,k):
    new_number=[]
    for i in range(0,len(number)-1):
        if rem_count==k:
            break
        if number[i]<number[i+1]:
            number[i]=-1
            rem_count+=1
    for j in range(0,len(number)):
        if number[j]!=-1:
            new_number.append(number[j])
    
    return new_number,rem_count
