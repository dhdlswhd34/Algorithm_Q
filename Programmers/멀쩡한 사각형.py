def solution(w,h):
    answer = 0
    temp =0
    # y = -(h/w)x +h 
    if(w == 1 or h ==1):
        return 0    
    elif(w  == h):
        return w*h-h
    for i in range(1,w):
        answer += int(-(h/w)*i +h)
        
    return answer*2