arr = []
for i in range(int(input())):
    age, name = map(str, input().split())
    arr.append([int(age), name])

arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])