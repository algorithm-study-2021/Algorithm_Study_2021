#카펫
def solution(brown, yellow):
    answer = []
    div=divisor(brown+yellow)
    
    for i in range(0,len(div)):
        if div[i]<3:
            continue
        else:
            if (div[i]-2)*(((brown+yellow)//div[i])-2)==yellow:
                answer.append(div[i])
                answer.append((brown+yellow)//div[i])
                answer.sort(reverse=True)
                break
    
    return answer

def divisor(num):
    div=[]
    for i in range(1,num+1):
        if num%i==0:
            div.append(i)    
    return div
