def solution(cacheSize, cities):
    time = 0
    if cacheSize==0:
        time=len(cities)*5
    else:
        time=cacheSize*5
        cache=[]
        for j in range(0,cacheSize):
            cache.append(cities[j].lower())
        for i in range(cacheSize,len(cities)):
            ex=cities[i].lower()
            if ex in cache: #cache hit
                cache.remove(ex)
                time+=1
            else: #cache miss
                del cache[0]
                time+=5
            cache.append(ex)
    return time
#cache hit: 도시 이름이 새로 들어왔을때, 기존에 있던 내용이면 실행시간 1추가+캐시 마지막으로 보냄
#cache miss: 도시 이름이 새로 들어왔을때, 기존에 없던 내용이면 가장 오래된 내용 제거+캐시 마지막으로 보냄+실행시간 5추가
#안됨ㅠㅠ
