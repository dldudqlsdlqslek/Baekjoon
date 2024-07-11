n = int(input())
for _ in range(n):
    a, b = input().split()
    c = ""
    for i in range(len(b)):
        c = c + b[i]*int(a)
    print(c)
