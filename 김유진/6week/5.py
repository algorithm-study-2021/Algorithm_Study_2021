def getLockedArr(n, arr):
    #arr 요소 하나를 n자리 이진수로 변경 -> 이에 대해 리스트 생성
    #중첩 리스트에 넣는 method 
    lockedArr=[]
    for i in arr:
        binary=format(i,'b')
        #길이 재서 부족한만큼 0 넣음
        addedZero=n-len(binary)
        binary='0'*addedZero+binary
        lockedArr.append(binary)
    return lockedArr

def solution(n, arr1, arr2):
    map1=getLockedArr(n,arr1)
    map2=getLockedArr(n,arr2)

    resArr=[]
    #어느 하나라도 1이면 1 둘 다 0이면 0
    for i in range(n):
        arrString=""
        for j in range(n):
            if map1[i][j]=='0' and map2[i][j]=='0':
                arrString+=' '
            else: arrString+='#'
        resArr.append(arrString)

    return resArr

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))