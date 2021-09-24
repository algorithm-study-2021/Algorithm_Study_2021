def thisIsNotNum(c):
    if c==' ' or c=='-' or c=='.' or (ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122):
        return True
    return False

#파일명 3개로 나누는 함수 (,,)으로 리스트 사용
def fileArr(fileArr):
    file_HNT_Arr=[]
    for file in fileArr:
        divided=False
        fileRes=[]
        numStart=0

        #숫자를 기준으로 나누기
        for i in range(len(file)):
            if divided==False and file[i]>='0' and file[i]<='9':
                fileRes.append(file[0:i]) 
                divided=True
                numStart=i

            if divided==True and thisIsNotNum(file[i]): #숫자 나왔다가 처음으로 문자 나오는 경우(TAIL부분)
                fileRes.append(int(file[numStart:i]))
                fileRes.append(file[i:])
                fileRes.append(file[numStart:i]) #숫자로 변환하지 않은 숫자(사실은 문자열) 마지막에
                break

        #TAIL이 Null인 경우
        if divided==True and len(fileRes)==1:
            fileRes.append(int(file[numStart:])) #비교위해 int값
            fileRes.append('')
            fileRes.append(file[numStart:]) #실제 쓸 str값 (마지막에 넣어주기 )

        file_HNT_Arr.append(fileRes)

    return file_HNT_Arr

def fileSort(file_HNT_Arr):

    file_HNT_Arr.sort(key=lambda x:(x[0].upper(),x[1]))
    #모든 파일명->배열로 정리 된 것을 다시 문자열(파일명)으로 변경
    for i in range(len(file_HNT_Arr)):
        file_HNT_Arr[i]=file_HNT_Arr[i][0]+file_HNT_Arr[i][3]+file_HNT_Arr[i][2]

    return file_HNT_Arr

def solution(files):
    files_to_arr=fileArr(files)
    return fileSort(files_to_arr)

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))