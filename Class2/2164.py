import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
c = deque(range(1, n+1))

while len(c) > 1:
    c.popleft()
    c.append(c.popleft())

print(c[0])
