def solution(n):
    i=1
    num=0
    while(1):
        if i>n:
            return num
        total=0
        for j in range(i,n+1):
            total+=j
            if total==n:
                num+=1
                break
            elif total>n:
                break
        i+=1

print(solution(15))