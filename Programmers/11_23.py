# https://www.acmicpc.net/problem/1904
def Q1904():
    count = [1,2]
    n = int(input())
    for i in range(2, n):
        count.append((count[i - 1]+count[i - 2]) % 15746)
    print(count[n - 1])

# https://www.acmicpc.net/problem/11053
def Q11053():
    n = int(input())
    arr = input()
    arr = arr.split(' ')

    count_arr = [1] * n

    for i in range(0, n):
        temp = []
        for j in range(0, i):
            if arr[i] > arr[j]:
                temp.append(count_arr[j] + 1)
        if len(temp) > 0:
            count_arr[i] = max(temp)
    print(max(count_arr))


# https://www.acmicpc.net/problem/12865
def Q12865():
    n, m = input().split()
    item = []
    for i in range(0, int(n)):
        item.append(input().split())

    


if __name__ == '__main__':
    Q12865()
