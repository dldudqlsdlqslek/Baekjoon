a = int(input())
b = int(input())
c = int(input())
n = str(a*b*c)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in n:
    count[int(i)] = count[int(i)]+1
for i in range(10):
    print(count[i])
