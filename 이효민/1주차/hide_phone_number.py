def solution(phone_number):
    num=len(phone_number) #전화번호 길이
    
    new_number=[]
    for i in range(0,num-4):
        new_number.append("*")
    for j in range(num-4,num):
        new_number.append(phone_number[j])
        
    answer = ''.join(new_number)
    return answer
