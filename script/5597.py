arr = [0 for _ in range(30)]
for i in range(28):
    arr[int(input()) - 1] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        print(i+1)