def solution(n,words):
    wordPool=[]
    idx=0

    while(idx<len(words)):
        if(idx==0): wordPool.append(words[idx]);idx+=1;continue 

        #비교
        if(words[idx] in wordPool) or (words[idx][0]!=words[idx-1][-1]):
            return [idx%n+1,idx//n+1]
        

        wordPool.append(words[idx])
        idx+=1

    return [0,0]

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
        