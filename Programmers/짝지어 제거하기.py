#코딩테스트 연습 2017 팁스타운 짝지어 제거하기

def solution(s):
    stack = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for value in s:
        if not stack:
            stack.append(value)
        else:
            if (stack[-1] == value):
                stack.pop()
            else:
                stack.append(value)
    
    if not stack:
        return 1
    else:
        return 0
                
