def search(num):
    b=format(num,'b')
    length=len(b)
    #뒤에서부터 0 있으면 1로 변경
    for i in range(length-1,-1,-1):
        print(b[i],", ",i)
        if b[i]=='0': 
            return num+2**(length-1-i)-2**(length-1-i-1) #0인거 1로 바꾸고 그 뒤 0으로 (제일 작은 거 구하기 위함 )

    #모두 1인 경우는 새로운 bit 1 -> 큰 하나 0으로
    return num-2**(length-1)+2**length

def solution(numbers):
    res=[]
    for i in numbers:
        if i%2==0: res.append(i+1) #짝수 
        else: res.append(search(i))

    return res

print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))