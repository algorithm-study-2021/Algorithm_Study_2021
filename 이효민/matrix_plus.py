def solution(arr1, arr2):
    answer = []
    
    for i in range(0,len(arr1)):
        lil_answer=[]
        for j in range(0,len(arr1[0])):
            lil_answer.append(arr1[i][j]+arr2[i][j])
        answer.append(lil_answer)
    
    return answer
