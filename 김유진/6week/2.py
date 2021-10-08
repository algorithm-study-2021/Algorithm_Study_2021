def solution(skill, skill_trees):
    skillLis=[]
    skill=list(skill)

    success=0;
    isCorrect=True
    for i in skill_trees: #i가 하나의 스킬트리 
        idx=0
        for j in i:
            if j in skill:
                if idx<skill.index(j):  
                    isCorrect=False;break
                else: idx+=1
        
        if isCorrect==True: success+=1 
        else: isCorrect=True
        
    return success