import sys

def mround(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())
if n == 0:
    diff = 0
else:
    dfs = []
    for _ in range(n):
        t = int(sys.stdin.readline())
        dfs.append(t)
    dfs.sort()
    ex = mround(len(dfs)*0.15)
    if ex != 0:
        dfs = dfs[ex:-ex]
    diff = mround(sum(dfs)/(n-2*ex))

print(diff)
