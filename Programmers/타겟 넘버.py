def find_a(arr1,arr2,target):
    answer = 0
    if not arr1:
        for value in arr2:
            if(target == value):
                answer += 1
    else:
        for value in arr1:
            if(target == value):
                answer += 1
    return answer

def solution(numbers, target):
    answer = 0
    arr1 = []
    arr2 = []
    
    #sum , len, lv
    s  = 0 
    l  = 0
 
    arr1.append(numbers[l])
    arr1.append(-numbers[l])
    l += 1    
    while(True):
        if(l%2):
            for value in arr1:
                arr2.append(value+numbers[l])
                arr2.append(value-numbers[l])
            arr1.clear()
            l += 1
        else:
            for value in arr2:
                arr1.append(value+numbers[l])
                arr1.append(value-numbers[l])
            arr2.clear()
            l += 1
        if(l == len(numbers)):
            answer = find_a(arr1,arr2,target)
            return answer