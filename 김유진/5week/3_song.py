def playingTime(m_info): #실제 재생시간
    #인자- list
    start=m_info[0]
    end=m_info[1]

    #재생시간 구하기
    hour=int(end[:2])-int(start[:2])
    min=int(end[3:])-int(start[3:])

    #예외 없음 (인자 자체가 True)
    return hour*60+min #분 기준으로 return 

def makeRepeat(length,melody):
    factor=melody.split() #모든 문자가 요소 

    index=0;
    while len(melody)<=length:
        if index==len(factor):
            index=0

        melody+=factor[index]
        index+=1

    return melody

def solution(m, musicinfos):
    # #처리 -> 소문자 변경 
    m=m.replace('C#','c')
    m=m.replace('D#','d')
    m=m.replace('F#','f')
    m=m.replace('G#','g')
    m=m.replace('A#','a')
    m=m.replace('B#','b')
    #일단 했는데 끔찍하니까 후에 바꾸기 

    song=[] #후보 리스트
    for m_info in musicinfos:
        m_info=m_info.split(',') #리스트로 변환 

        #노래코드 소문자로 변경 (개끔찍하니까 바꾸기 )
        m_info[3]=m_info[3].replace('C#','c')
        m_info[3]=m_info[3].replace('D#','d')
        m_info[3]=m_info[3].replace('F#','f')
        m_info[3]=m_info[3].replace('G#','g')
        m_info[3]=m_info[3].replace('A#','a')
        m_info[3]=m_info[3].replace('B#','b')

        #m_info의 노래코드를 m_info의 재생시간만큼 조정
        if len(m_info[3])<playingTime(m_info):
            m_info[3]=makeRepeat(playingTime(m_info),m_info[3])
        if len(m_info[3])>playingTime(m_info):
            m_info[3]=m_info[3][:playingTime(m_info)]

        if m in m_info[3]:
            song.append(m_info)

    #후보 끝
    if len(song)==0: return "(None)"

    #재생시간으로 정렬
    song.sort(key=lambda x:-(playingTime(x))) 
    #재생시간 같은 경우, 먼저 나온 거 반환 

    return song[0][2]