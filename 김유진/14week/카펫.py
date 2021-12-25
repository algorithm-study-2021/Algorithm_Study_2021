def solution(brown, yellow):

    for s in range(1,yellow+1,1):
        if yellow%s==0:
            print(s)
            #총 필요한 b블럭 계산
            x=s; y=yellow//s #x; 가로 y- 세로
            if y>x: x,y=y,x

            block=x*2+(y+2)*2

            if block==brown:
                return [x+2,y+2]