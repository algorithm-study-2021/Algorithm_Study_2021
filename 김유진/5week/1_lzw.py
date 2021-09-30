def solution(msg):
    #기본 구성
    dictionary=[' ']+list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    buf="" #버퍼 역할 
    offset=0
    res=[]
    
    while 1:
        #종료조건 적어줘야함(일단 skip)

        #현재 offset부터 dict에 있는 단어까지만 buf에 넣어줌
        buf+=msg[offset]
        while 1:
            try:
                if buf+msg[offset+1] in dictionary:
                    offset+=1
                    buf+=msg[offset]
                else: break
            except: #offset+1 range 오류
                if buf in dictionary:
                    res.append(dictionary.index(buf))
                else:
                    dictionary.append(buf)
                    res.append(dictionary.index(buf))
                return res

        res.append(dictionary.index(buf))
        dictionary.append(buf+msg[offset+1])

        offset+=1
        buf=""

    return res
