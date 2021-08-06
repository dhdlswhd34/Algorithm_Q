def solution(n, computers):
    answer = 0
    temp = 0
    
    #대각선 검사
    for i in range(n):
        temp = i
        if(computers[temp][temp] == 1):
            computers[temp][temp] = 0  
            
            #한줄씩 검사
            for j in range(temp,n):
                if(computers[temp][j] == 1):
                    computers[temp][j] = 0
                    temp = j
                    computers[temp][temp] = 0
            #+1
            answer += 1
            
        
    return answer