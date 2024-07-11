n, k = map(int, input().split())
fin = []
q = list(range(1, n+1))
i = 0
while q:
    i = (i+k-1)%len(q)
    fin.append(q.pop(i))
print("<" + ", ".join(map(str, fin)) + ">")
