a = [-1 for _ in range(26)]
l = input()
for i in range(len(l)):
    if a[ord(l[i])-97] == -1:
        a[ord(l[i])-97] = i
for j in range(26):
    print(a[j], end = ' ')
