"""
재귀 사용
answer=[0,1] 첫번째 0 횟수 두번째 1 횟수

2차원 배열 슬라이싱 하는 법
[row[j:j+m] for row in field[i:i+n]]
"""
def checkArr(arr,answer): #수행할 배열, 정답 넣는 배열
    n=len(arr)
    if n==1:
        #중첩 리스트 형태로 들어있음 1개이긴 한데 리스트임 
        answer[arr[0][0]]+=1 #증가 
        return 

    #들어온 answer 배열 모두 같은지 확인
    standardArr=arr[0][0]
    zipCheck=True
    keepgoing=True
    for i in arr:
        if keepgoing is False: break
        for j in i:
            if j!=standardArr: 
                zipCheck=False
                keepgoing=False ; break
    
    if zipCheck==True: answer[standardArr]+=1 ; return 
    else: 
        n=n//2
        #4개로 나눠서 여부 검사
        checkArr([i[:n] for i in arr[:n]],answer) #1
        checkArr([i[n:] for i in arr[:n]],answer) #2
        checkArr([i[:n] for i in arr[n:]],answer) #3
        checkArr([i[n:] for i in arr[n:]],answer) #4

def solution(arr):
    answer=[0,0]
    checkArr(arr,answer)

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))