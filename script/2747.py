n = int(input())
d = [0] * (n+1)

if n == 1:
    d[1] = 1
    print(d[1])
elif n == 2:
    d[2] = 1
    print(d[2])
else:
    d[1] = 1
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
    print(d[n])