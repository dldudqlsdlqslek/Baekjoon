a = []
cnt = 0
for i in range(10):
    n = int(input())
    r = n%42
    if r not in a:
        cnt = cnt + 1
        a.append(r)
print(cnt)
