from collections import Counter
import sys

n = int(sys.stdin.readline())
ns = []
for _ in range(n):
    ns.append(int(sys.stdin.readline()))
    
ns.sort()
count = Counter(ns).most_common()

print(round(sum(ns)/len(ns)))
print(ns[n//2])
if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(max(ns) - min(ns))
