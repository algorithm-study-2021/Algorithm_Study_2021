def solution(arr1, arr2):
    answer=[]
    
    for r in range(len(arr1)):
        temp=[]
        for l in range(len(arr1[0])):
            temp.append(arr1[r][l]+arr2[r][l])
        answer.append(temp)
        
    return answer