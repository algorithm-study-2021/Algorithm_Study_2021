#이름은 일부러 문제 번호로 설정

def solution(s):
    countP=0; countY=0
    for i in s:
        if i=='p' or i=='P': countP+=1
        elif i=='y' or i=='Y':countY+=1

    if countP!=countY: return False 

    return True