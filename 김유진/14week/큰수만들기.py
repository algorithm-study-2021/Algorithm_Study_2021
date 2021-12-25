def solution(number, k):

    number=list(number)
    stack=[]
    count=0; index=0

    while 1:
        #종료 조건
        if count==k:
            stack+=number[index:]
            break

        #count==k를 만족하지 않고 number가 끝나는 경우 
        if index==len(number): 
            offset=k-count
            stack=stack[:len(number)-offset] #앞에 더 큰 수가 있도록 설계했기 때문 
            break

        #핵심 알고리즘
        if len(stack)==0:
            stack.append(number[index]); index+=1
        
        elif stack[-1]>=number[index]:
            stack.append(number[index]); index+=1
        
        elif stack[-1]<number[index]:
            stack.pop(-1); count+=1

    return ''.join(stack)
