def solution(board, moves):
    answer = 0
    bk = [0]

    for value in moves:
        for arr in board:
            temp = arr[value-1]
            if temp:
                if bk[-1] == temp:
                    del bk[-1]
                    answer += 2
                else:
                    bk.append(temp)
                arr[value-1] = 0
                break
    return answer