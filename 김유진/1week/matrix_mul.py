#행렬의 곱셈 
def solution(arr1, arr2):
    row=len(arr1)
    col=len(arr2[0])

    result=[]

    for r in range(row):
        row_result=[]
        for c in range(col):
            #곱해서 값 생성
            temp=0
            for t in range(len(arr1[0])):
                temp+=arr1[r][t]*arr2[t][c]

            row_result.append(temp)
        result.append(row_result)
        
    return result

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))