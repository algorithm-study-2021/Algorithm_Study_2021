def putValue(res,nowDart,putnewDart):
    if nowDart=='S': res.append(int(putnewDart))
    elif nowDart=='D': res.append(pow(int(putnewDart),2))
    elif nowDart=='T': res.append(pow(int(putnewDart),3))

def solution(dartResult):
    res=[]

    index=0;
    while 1:
        nowDart=dartResult[index]
        if nowDart in ['S','D','T']:
            #10점 고려
            try:
                if dartResult[index-2]>='0' and dartResult[index-2]<='9':
                    if nowDart=='S': res.append(10)
                    elif nowDart=='D': res.append(100)
                    elif nowDart=='T': res.append(1000)
            except:
                putValue(res,nowDart,dartResult[index-1])

            else:
                putValue(res,nowDart,dartResult[index-1])

        #특별상
        elif nowDart =='*':
            if len(res)==1: res[0]*=2
            else: res[-1]*=2; res[-2]*=2

        elif nowDart=='#':
            res[-1]*=-1

        index+=1

        if(index==len(dartResult)): break
    
    return sum(res)

print(solution("1S*2T*3S"))