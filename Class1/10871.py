a, b = map(int, input().split())
w = input().split()
for i in w:
    if int(i)<b:
        print(i, end = ' ')
