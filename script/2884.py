time = list(map(int, input().split()))

if time[1] < 45:
    if time[0] == 0:
        time[0] = 23
        time[1] += 60
    else:
        time[0] -= 1
        time[1] += 60

print(time[0], time[1]-45)