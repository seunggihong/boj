arr = []
for i in range(int(input())):
    x, y = map(int, input().split())
    arr.append([x,y])

arr.sort(key=lambda x: (x[0],x[1]))
for i in arr:
    print(i[0], i[1])