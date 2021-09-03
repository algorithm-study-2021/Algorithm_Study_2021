def solution(arr1, arr2):
    answer = []
    num1=len(arr1) #answer 세로값
    num2=len(arr2) #answer 가로값
    
    new_arr2=[]
    for i in range(0,len(arr2[0])):
        lil_new_arr2=[]
        for j in range(0,num2):
            lil_new_arr2.append(arr2[j][i])
        new_arr2.append(lil_new_arr2)
    
    cha_answer=[]
    for k in range(0,len(new_arr2)):
        lil_answer=[]
        for f in range(0,num1):
            lil_answer.append(multiply_array(arr1[f],new_arr2[k]))
        cha_answer.append(lil_answer)
    
    for m in range(0, len(cha_answer[0])):
        lil_answer=[]
        for p in range(0, len(cha_answer)):
            lil_answer.append(cha_answer[p][m])
        answer.append(lil_answer)
    
    return answer

def multiply_array(ar1,ar2):
    result=0
    for i in range(0,len(ar1)):
        result+=ar1[i]*ar2[i]
    
    return result
