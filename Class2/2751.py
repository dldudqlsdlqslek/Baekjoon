import sys

n = int(sys.stdin.readline().rstrip())
ns = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    ns.append(a)

ns.sort()
for i in range(n):
    print(ns[i])
