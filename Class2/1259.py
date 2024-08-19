while True:
    flag = 0
    n = input()
    if n == '0':
        break
    l = len(n)
    for i in range(l//2):
        if n[i] != n[l-1-i]:
            flag = 1
    if flag == 0:
        print("yes")
    else:
        print("no")
