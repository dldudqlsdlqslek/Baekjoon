n = int(input())
a = list(map(int, input().split()))
total = 0
m = max(a)
for i in range(n):
    a[i] = a[i]/m * 100
    total = total + a[i]
print(total/n)
