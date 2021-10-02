def solution(dirs):
    dirs=list(dirs)
    move=0
    x=0
    y=0
    his=[]
    for i in range(0,len(dirs)):
        spot=[]
        re_spot=[]
        if dirs[i]=='U' and y<5:
            y+=1
            spot=[x,y,x,y-1]
            re_spot=[x,y-1,x,y]
        elif dirs[i]=='D'and y>-5:
            y-=1
            spot=[x,y,x,y+1]
            re_spot=[x,y+1,x,y]
        elif dirs[i]=='R' and x<5:
            x+=1
            spot=[x,y,x-1,y]
            re_spot=[x-1,y,x,y]
        elif dirs[i]=='L'and x>-5:
            x-=1  
            spot=[x,y,x+1,y]
            re_spot=[x+1,y,x,y]
        if (spot in his)==False and (re_spot in his)==False and spot:
            move+=1
        his.append(spot)
        
    answer=move
    return answer
