n = int(input())
a = set(map(int, input().split()))

m = int(input())
finds = list(map(int, input().split()))

for i in finds:
    if i in a:
        print(1)
    else:
        print(0)
