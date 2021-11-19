#stack으로 구현
def solution(prices):
    stack=[(0,prices[0])]
    res=[-1 for i in range(len(prices))]

    for i in range(1,len(prices)):

        while len(stack)!=0 and stack[-1][1]>prices[i]:
            factor=stack.pop()
            res[factor[0]]=i-factor[0]
 
        stack.append((i,prices[i]))

    #남은 stack, res에 적용
    while len(stack)!=0:
        factor=stack.pop()
        res[factor[0]]=len(prices)-1-factor[0]

    return res

print(solution([1, 3, 5, 7, 9, 4, 5, 2, 1, 0]))