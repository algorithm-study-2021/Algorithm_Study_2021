def solution(strings, n):
    answer = []
    strings.sort()
    
    arr=[]
    for i in range(0,len(strings)):
        arr.append([strings[i][n],strings[i]])
    arr=sorted(arr)
    
    for j in range(0,len(strings)):
        answer.append(arr[j][1])
    
    return answer
