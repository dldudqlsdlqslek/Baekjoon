def countLan(lans, lenn):
    count = 0
    for i in lans:
        count += i // lenn
    return count

def binaryFind(lans, n):
    st = 1
    ed = max(lans)

    while st <= ed:
        md = (st + ed) // 2
        count = countLan(lans, md)

        if count >= n:
            st = md + 1
        else:
            ed = md - 1

    return ed

k, n = map(int, input().split())
lans = []
for _ in range(k):
    lan = int(input())
    lans.append(lan)
m = binaryFind(lans, n)
print(m)
