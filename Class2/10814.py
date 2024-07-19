import sys

n = int(sys.stdin.readline().rstrip())
man = []

for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    man.append((int(age), name))

man.sort(key=lambda x: (x[0], _))

for i in man:
    print(i[0], i[1])
