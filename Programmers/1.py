def solution(board, moves):
    answer = 0
    
    bk = [0]
    
    for value in moves:
        while True:
            if not board[value-1]:
                break
            temp = board[value-1].pop()
            if temp != 0:
                if bk[-1] == temp:
                    del bk[-1]
                    answer += 2
                else:
                    bk.append(temp)
                break
                
    #print(board)
    return answer