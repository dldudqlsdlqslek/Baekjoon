l = input()
c = l.count(' ') + 1
if l[0] == ' ':
    c = c -1
if l[len(l)-1] == ' ':
    c = c - 1
print(c)
