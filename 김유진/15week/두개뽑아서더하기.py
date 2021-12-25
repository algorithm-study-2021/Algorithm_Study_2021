def solution(numbers):
    answer=[]
    
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum=numbers[i]+numbers[j]
            if sum not in answer:
                answer.append(sum)

    return sorted(answer)

print(solution([2,1,3,4,1]))