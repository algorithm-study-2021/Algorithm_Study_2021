def solution(a, b):
    day=0
    callendar=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,a-1):
        day+=callendar[i]
    day+=b

    day%=7
    if day==1: return 'FRI'
    elif day==2: return 'SAT'
    elif day==3: return 'SUN'
    elif day==4: return 'MON'
    elif day==5: return 'TUE'
    elif day==6: return 'WED'
    else: return 'THU'
