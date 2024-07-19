t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prints = list(map(int, input().split()))
    q = list(enumerate(prints))
    count = 0

    while q:
        doc = q.pop(0)
        if any(doc[1] < i for _, i in q):
            q.append(doc)
        else:
            count += 1
            if doc[0] == m:
                print(count)
