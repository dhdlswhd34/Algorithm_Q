# 문제 1번
# def dynamicsum(n):
#     if n == 1:   return 1
#     elif n == 2: return 2
#     elif n == 3: return 4
#     else:
#         return dynamicsum(n-1) + dynamicsum(n-2) + dynamicsum(n-3)

# n = int(input())

# for i in range(n):
#     num = int(input())
#     print(dynamicsum(num))



# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10

# def right(result):
#     result[x][y+1]

# def up():

r, c = input().split()
temp = []
result = []
print(r, c)
for i in range(int(r)):
    a, b, c, d, e = input().split()
    result.append([a, b, c, d, e])

temp = lambda x, y: result[x][y + 1]
print(result)
print(temp(0,0))

#     print(dynamicsum(num))


