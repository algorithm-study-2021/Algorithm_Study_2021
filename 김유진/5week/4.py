def solution(dirs):
    #현재 좌표
    x=0
    y=0
    res=set() #반대로 들어간 건 마지막에 빼줄 거임 
    for i in dirs:
        print('좌표:',x,", ",y)
        if i=='U':
            if y+1 <=5:
                if ((x,y+1),(x,y)) not in res:
                    nowcd=((x,y),(x,y+1))
                    res.add(nowcd)
                y+=1
        elif i=='D' :
            if y-1>=-5:
                if ((x,y-1),(x,y)) not in res:
                    nowcd=((x,y),(x,y-1))
                    res.add(nowcd)
                y-=1
        elif i=='R':
            if x+1<=5:
                if ((x+1,y),(x,y)) not in res:
                    nowcd=((x,y),(x+1,y))
                    res.add(nowcd)
                x+=1
        elif i=='L':
            if x-1>=-5:
                if ((x-1,y),(x,y)) not in res:
                    nowcd=((x,y),(x-1,y))
                    res.add(nowcd)
                x-=1
        print(res)

    return len(res)

print(solution("UDU"))