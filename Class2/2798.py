n, m = map(int, input().split())
a = list(map(int, input().split()))
max = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            if a[i] + a[j] + a[k] <= m:
                if a[i] + a[j] + a[k] > max:
                    max = a[i] + a[j] + a[k]
print(max)
